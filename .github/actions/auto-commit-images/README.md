# Auto-commit Base images

Base images are in the folder `data/00000X/32/*`. They are generated automatically from Gold images. This action detects:

* Detects newly added or updated images
* Pushes them to the DVC storage
* And generates a signed commit to add them to the repository

The corresponding command if you want to do it manually is:

```
dvc add 
git add data/000001/32/000001-42.600.2.tif
dvc push
git add data/000001/32/000001-42.600.2.tif data/000001/32/000004-32.600.2.tif.dvc data/000001/32/.gitignore
git commit -S -m "Add new Base image: 000001-42.600.2.tif"
git push
```

Commits are created by using GitHub API: https://gist.github.com/swinton/03e84635b45c78353b1f71e41007fc7c

## Usage

You need to add the action in your workflow:

```yaml
- name: Auto-commit added or modified images
  id: auto-commit
  uses: ./.github/actions/auto-commit-images
  with:
    repository: "${{ github.repository }}"
    repo_dir: "${{ github.workspace }}"
    repo_token: "${{ secrets.GITHUB_TOKEN }}"
    branch: "${{ github.ref }}"
```

### Inputs

| Input        | Description                                                     |
|--------------|-----------------------------------------------------------------|
| `repository` | The owner and repository name. For example, octocat/Hello-World |
| `repo_dir`   | The git repo root dir                                           |
| `repo_token` | The auto-generated GitHub token                                 |
| `branch`     | The branch where we want to add the commit                      |

### Outputs

| Input              | Description                       |
|--------------------|-----------------------------------|
| `changes_detected` | True if files have been committed |

### Development

> IMPORTANT: this sample commands have to be executed from `.github/actions/auto-commit-images` folder.

> You can use [act](https://github.com/nektos/act) to run the action locally within a workflow.

Build docker image:
```
docker build --no-cache -t act-github-actions-auto-commit-images:latest .
```

Run GitHub action locally with docker:
```
docker run --rm -it \
  --env INPUT_REPOSITORY=Nautilus-Cyberneering/chinese-ideographs \
  --env INPUT_REPO_DIR=/repo \
  --env INPUT_REPO_TOKEN=XXX \
  --env INPUT_BRANCH=main \
  --volume $(pwd)/src:/app \
  --volume $(pwd)/../../..:/repo \
  act-github-actions-auto-commit-images
```

Show dvc version:
```
docker run --rm -it act-github-actions-auto-commit-images dvc --version
```

Check linting for `Dockerfile`:
```
docker run --rm -i hadolint/hadolint < ./Dockerfile
```

### Testing

Build docker image:
```
docker build --target testing --no-cache -t  act-github-actions-auto-commit-images-test .
```

Run tests:
```
docker run --rm \
  --volume $(pwd)/src:/app \
  act-github-actions-auto-commit-images-test pytest
```
