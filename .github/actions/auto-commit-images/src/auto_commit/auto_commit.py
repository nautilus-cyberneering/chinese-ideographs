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


def add_new_base_images_to_the_repo(local_repo, repository, repo_dir, repo_token, repo_base_image_paths, branch_ref):
    # https://github.com/PyGithub/PyGithub/issues/1628

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
        commit_message = f'Add Base image {repo_base_image_path}'

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

        blob1 = remote_repo.create_git_blob(base_image_pointer_path, "utf-8")
        element1 = github.InputGitTreeElement(
            path=repo_base_image_pointer_path, mode='100644', type='blob', sha=blob1.sha)
        blob2 = remote_repo.create_git_blob(base_image_gitignore_path, "utf-8")
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
    os.system('dvc push')


def dvc_delete_and_push_image(repo_dir, repo_base_image):
    ''' Delete Base image from dvc and push to remote storage'''
    cmd = f'cd {repo_dir} && dvc delete {repo_base_image}'
    print(cmd)
    os.system(cmd)
    os.system('dvc push')


def auto_commit(repository, repo_dir, repo_token, branch):
    local_repo = Repo(repo_dir)

    print_debug_info(repo_dir, local_repo)

    # New Base images
    added_repo_base_image_paths = get_new_base_images(local_repo)
    print("Added Base images: ", added_repo_base_image_paths)

    # dvc add and push
    for repo_base_image in added_repo_base_image_paths:
        dvc_add_and_push_image(repo_dir, repo_base_image)

    # git commit Base image: dvc pointer, and .gitignore
    commits_for_added_images = add_new_base_images_to_the_repo(
        local_repo, repository, repo_dir, repo_token, added_repo_base_image_paths, branch)

    return commits_for_added_images