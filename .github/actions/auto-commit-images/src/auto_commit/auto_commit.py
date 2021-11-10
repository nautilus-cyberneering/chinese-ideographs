import base64
import os

import github
from git import Repo

from auto_commit.librarian import (LibraryFilename, filter_base_images,
                                   filter_media_library_files)


class FileNotFoundInRepoException(Exception):
    """Raised when we try to get the sha of a non-existing file file"""
    pass


def print_repo_dir(repo_dir):
    print("repo: ", repo_dir)


def print_git_diff(repo):
    # https://git-scm.com/docs/git-diff#Documentation/git-diff.txt---diff-filterACDMRTUXB82308203

    for diff_added in repo.index.diff(None).iter_change_type('A'):
        print("Added:     ", diff_added.a_path)

    for diff_copied in repo.index.diff(None).iter_change_type('C'):
        print("Copied     ", diff_copied.a_path)

    for diff_deleted in repo.index.diff(None).iter_change_type('D'):
        print("Deleted:   ", diff_deleted.a_path)

    for diff_renamed in repo.index.diff(None).iter_change_type('R'):
        print("Renamed:   ", diff_renamed.a_path)

    for diff_modified in repo.index.diff(None).iter_change_type('M'):
        print("Modified:  ", diff_modified.a_path)

    for diff_changed in repo.index.diff(None).iter_change_type('T'):
        print("Changed:   ", diff_changed.a_path)


def print_git_untracked(repo):
    for untracked in repo.untracked_files:
        print("Untracked: ", untracked)


def print_debug_info(repo_dir, repo):
    print_repo_dir(repo_dir)
    print_git_untracked(repo)
    print_git_diff(repo)


def get_all_modified_files(repo):
    all_modified_files = []
    for diff_modified in repo.index.diff(None).iter_change_type('M'):
        all_modified_files.append(diff_modified.a_path)
    return all_modified_files


def get_all_deleted_files(repo):
    all_deleted_files = []
    for diff_deleted in repo.index.diff(None).iter_change_type('D'):
        all_deleted_files.append(diff_deleted.a_path)
    return all_deleted_files


def get_new_base_images(repo):
    all_untracked_files = repo.untracked_files
    return filter_base_images(filter_media_library_files(all_untracked_files))


def get_modified_base_images(repo):
    all_modified_files = get_all_modified_files(repo)
    return filter_base_images(filter_media_library_files(all_modified_files))


def get_deleted_base_images(repo):
    all_deleted_files = get_all_deleted_files(repo)
    return filter_base_images(filter_media_library_files(all_deleted_files))


def add_or_modify_base_images_in_git(repository, repo_dir, repo_token, repo_base_image_paths, branch_ref, commit_prefix):
    gh = github.Github(repo_token)

    remote_repo = gh.get_repo(repository)

    commits = []

    for repo_base_image_path in repo_base_image_paths:

        # Files we have to include in the commit:
        # data/000001/42/000001-42.600.2.tif.dvc  (dvc pointer)
        # data/000001/42/.gitignore               (dvc .gitignore)

        # Relative paths
        repo_base_image_pointer_path = repo_base_image_path + '.dvc'
        repo_base_image_gitignore_path = os.path.dirname(
            repo_base_image_path) + '/.gitignore'

        # Absolute paths
        base_image_path = f'{repo_dir}/{repo_base_image_path}'
        base_image_pointer_path = f'{repo_dir}/{repo_base_image_pointer_path}'
        base_image_gitignore_path = f'{repo_dir}/{repo_base_image_gitignore_path}'

        # Commit message
        base_image_filename = os.path.basename(repo_base_image_path)
        commit_message = f'{commit_prefix} {base_image_filename}'

        branch = os.path.basename(branch_ref)

        # Debug info
        print("Auto-commit to add Base image: ")
        print("Repo dir: ", repo_dir)
        print("Base image path: ", base_image_path)
        print("Base image pointer path: ", base_image_pointer_path)
        print("Base iamge gitignore path: ", base_image_gitignore_path)
        print("Commit message: ", commit_message)
        print("Branch ref: ", branch_ref)
        print("Branch: ", branch)

        # Create git tree elements

        content1 = open(base_image_pointer_path, "r").read()
        blob1 = remote_repo.create_git_blob(content1, "utf-8")
        element1 = github.InputGitTreeElement(
            path=repo_base_image_pointer_path, mode='100644', type='blob', sha=blob1.sha)

        content2 = open(base_image_gitignore_path, "r").read()
        blob2 = remote_repo.create_git_blob(content2, "utf-8")
        element2 = github.InputGitTreeElement(
            path=repo_base_image_gitignore_path, mode='100644', type='blob', sha=blob2.sha)

        elements = [element1, element2]

        head_sha = remote_repo.get_branch(branch).commit.sha
        print("Branch head sha: ", head_sha)

        base_tree = remote_repo.get_git_tree(sha=head_sha)
        print("Base tree: ", base_tree)

        tree = remote_repo.create_git_tree(elements, base_tree)
        print("Tree: ", tree)

        parent = remote_repo.get_git_commit(sha=head_sha)
        print("Parent: ", parent)

        commit = remote_repo.create_git_commit(commit_message, tree, [parent])
        print("New commit: ", commit)

        branch_refs = remote_repo.get_git_ref(f'heads/{branch}')
        print("Banch refs: ", branch_refs)

        branch_refs.edit(sha=commit.sha)
        print("New branch ref: ", commit.sha)

        commits.append(commit.sha)

    return commits


def dvc_add_and_push_image(repo_dir, repo_base_image):
    ''' Add Base image to dvc and push to remote storage'''
    cmd = f'cd {repo_dir} && dvc add {repo_base_image}'
    print(cmd)
    os.system(cmd)
    # TODO: maybe we should push after commiting. If the git commit fail we will have those images in the remote storage but not in the git repo.
    # We can also execute dvc garbage collectro in a different workflow, to clean the dvc storage periodically.
    # Discussion: https://github.com/Nautilus-Cyberneering/chinese-ideographs/discussions/101
    os.system('dvc push')


def dvc_delete_local_and_remote_image(repo_dir, repo_base_image):
    ''' Delete Base image from dvc'''
    cmd = f'cd {repo_dir} && dvc remove {repo_base_image}'
    print(cmd)
    os.system(cmd)


def commit_added_base_images(local_repo, repository, repo_dir, repo_token, branch):
    # New Base images
    added_repo_base_image_paths = get_new_base_images(local_repo)
    print("Added Base images: ", added_repo_base_image_paths)

    # dvc add and push
    for repo_base_image in added_repo_base_image_paths:
        dvc_add_and_push_image(repo_dir, repo_base_image)

    # git commit Base image: dvc pointer, and .gitignore
    commits_for_added_images = add_or_modify_base_images_in_git(
        repository, repo_dir, repo_token, added_repo_base_image_paths, branch, 'Add Base image')

    return commits_for_added_images


def commit_modified_base_images(local_repo, repository, repo_dir, repo_token, branch):
    # Modified Base images
    modified_repo_base_image_paths = get_modified_base_images(local_repo)
    print("Modified Base images: ", modified_repo_base_image_paths)

    # dvc add and push
    for repo_base_image in modified_repo_base_image_paths:
        dvc_add_and_push_image(repo_dir, repo_base_image)

    # git commit Base image: dvc pointer, and .gitignore
    commits_for_modified_images = add_or_modify_base_images_in_git(
        repository, repo_dir, repo_token, modified_repo_base_image_paths, branch, 'Update Base image')

    return commits_for_modified_images


def commit_deleted_base_images(local_repo, repository, repo_dir, repo_token, branch):
    # Deleted Base images
    deleted_repo_base_image_paths = get_deleted_base_images(local_repo)
    print("Deleted Base images: ", deleted_repo_base_image_paths)

    # dvc remove
    for repo_base_image in deleted_repo_base_image_paths:
        # We have to use the dvc image pointer (.dvc) not the tiff image
        dvc_delete_local_and_remote_image(repo_dir, repo_base_image + '.dvc')

    # git commit Base image: dvc pointer, and .gitignore
    commits_for_deleted_images = add_or_modify_base_images_in_git(
        repository, repo_dir, repo_token, deleted_repo_base_image_paths, branch, 'Delete Base image')

    return commits_for_deleted_images


def auto_commit(repository, repo_dir, repo_token, branch):
    local_repo = Repo(repo_dir)

    print_debug_info(repo_dir, local_repo)

    commits_for_added_images = commit_added_base_images(
        local_repo, repository, repo_dir, repo_token, branch)

    commits_for_modified_images = commit_modified_base_images(
        local_repo, repository, repo_dir, repo_token, branch)

    commits_for_deleted_images = commit_deleted_base_images(
        local_repo, repository, repo_dir, repo_token, branch)

    # TODO: process renamed files. dvc diff could return an output like:
    # {added: [], deleted: [], modified: [], renamed: [{path: {old: data/000004/32/000004-32.600.2.tif, new: data/000005/32/000005-32.600.2.tif}}]}
    # when a Gold or Base image is renamed or when you delete and create a new image with the same content (same md5 has).
    # If we are renaming a GOld image we have to rename the corresponding Base image.
    # If we are using a different artwork id we should warning that the image content is the same and make the workflow fail.

    return commits_for_added_images + commits_for_modified_images + commits_for_deleted_images
