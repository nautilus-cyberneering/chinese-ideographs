import os
import json

from auto_commit.auto_commit import auto_commit


def main(repository, repo_dir, repo_token, branch):
    commits = auto_commit(repository, repo_dir, repo_token, branch)

    changes_detected = 'false'

    if len(commits) > 0:
        changes_detected = 'true'

    print(f'::set-output name=changes_detected::{changes_detected}')


if __name__ == "__main__":
    repository = os.environ["INPUT_REPOSITORY"]
    repo_dir = os.environ["INPUT_REPO_DIR"]
    repo_token = os.environ["INPUT_REPO_TOKEN"]
    branch = os.environ["INPUT_BRANCH"]
    main(repository, repo_dir, repo_token, branch)
