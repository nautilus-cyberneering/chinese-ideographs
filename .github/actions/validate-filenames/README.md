# Validate filename

Validate a list of filenames.

## Usage

You need to add the action in your workflow:

```yaml
- name: Validate filenames
  uses: ./.github/actions/validate-filenames
  with:
    filenames: '{"added": [{"path": "data/000001/32/000001-32.600.2.tif"}], "deleted": [], "modified": [], "renamed": []}'
```

### Inputs

| Input       | Description                           |
|-------------|---------------------------------------|
| `filenames` | Array in JSON with the list of paths  |                   |

### Outputs

No outputs.

### Development

> IMPORTANT: this sample commands have to be executed from `.github/actions/validate-filenames` folder, except for `act`commands.

Build docker image:
```
docker build --no-cache -t act-github-actions-validate-filenames .
```

Run GitHub action locally with docker:
```
docker run --rm -it \
  --env INPUT_FILENAMES='{"added": [{"path": "data/000001/32/000001-32.600.2.tif"}], "deleted": [], "modified": [], "renamed": []}' \
  --volume $(pwd)/src:/app \
  act-github-actions-validate-filenames
```

Run action using `act`:
```
act pull_request --job build
```

Delete previous cached docker image:
```
docker image rm act-github-actions-validate-filenames
```

### Testing

Build docker image:
```
docker build --target testing --no-cache -t  act-github-actions-validate-filenames-test .
```

Run tests:
```
docker run --rm \
  --volume $(pwd)/src:/app \
  act-github-actions-validate-filenames-test pytest
```

### Troubleshooting

Running this command `act pull_request -j build` you could get this error:
```
ADD failed: file not found in build context or excluded by .dockerignore: stat src: file does not exist
```
For some reason, the docker build fails. If you pre-build the image manually, it works. It seems the problem is inside `catthehacker/ubuntu` docker image.