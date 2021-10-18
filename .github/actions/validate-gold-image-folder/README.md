# Validate Gold image folder

Given a filepath list, it checks whether the files that are Gold images are in the correct folder or not.

The input format for the list is the [`dvd diff`](https://dvc.org/doc/command-reference/diff) command JSON format:

```json
{
  "added": [
    {
      "path": "data/000001/32/000001-32.600.2.tif"
    }
  ],
  "deleted": [],
  "modified": [],
  "renamed": []
}
```

It follows these [filename format and folder structure conventions](https://github.com/Nautilus-Cyberneering/chinese-ideographs/blob/main/documentation/Filenames_and_Folder_Structure_Conventions.md).

## Usage

You need to add the action in your workflow:

```yaml
- name: Validate filenames
  uses: ./.github/actions/validate-gold-image-folder
  with:
    filepaths: '{"added": [{"path": "data/000001/32/000001-32.600.2.tif"}], "deleted": [], "modified": [], "renamed": []}'
```

### Inputs

| Input       | Description                           |
|-------------|---------------------------------------|
| `file paths | Array in JSON with the path list      |

### Outputs

Process exception when validation fails.

### Development

> IMPORTANT: this sample commands have to be executed from `.github/actions/validate-gold-image-folder` folder.

> You can use [act](https://github.com/nektos/act) to run the action locally within a workflow.

Build docker image:
```
docker build --no-cache -t act-github-actions-validate-gold-image-folder:latest .
```

Run GitHub action locally with docker:
```
docker run --rm -it \
  --env INPUT_FILEPATHS='{"added": [{"path": "data/000001/32/000001-32.600.2.tif"}], "deleted": [], "modified": [], "renamed": []}' \
  --volume $(pwd)/src:/app \
  act-github-actions-validate-gold-image-folder
```

Check linting for `Dockerfile`:
```
docker run --rm -i hadolint/hadolint < ./Dockerfile
```

### Testing

Build docker image:
```
docker build --target testing --no-cache -t  act-github-actions-validate-gold-image-folder-test .
```

Run tests:
```
docker run --rm \
  --volume $(pwd)/src:/app \
  act-github-actions-validate-gold-image-folder-test pytest
```
