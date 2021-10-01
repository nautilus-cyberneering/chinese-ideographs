# Validate filename

Validate a list of filenames.

## Usage

You need to add the action in your workflow:

```yaml
- name: Validate filenames
  uses: ./.github/actions/validate-filenames
  with:
    filenames: "{[\"data/000001/32/000001-32.600.2.tif\"]}"
```

### Inputs

| Input       | Description                           |
|-------------|---------------------------------------|
| `filenames` | Array in JSON with the list of paths  |                   |

### Outputs

No outputs.

### Development

Build docker image:
```
docker build -t validate-filenames .
```

Run as GitHub action locally with docker:
```
docker run -it \
  --env INPUT_FILENAMES="{[\"data/000001/32/000001-32.600.2.tif\"]}" \
  --volume $(pwd):/github/workspace \
  validate-filenames
```

Run action using `act`:
```
act -j act pull_request
```

Delete previous cached docker image:
```
docker image rm act-github-actions-validate-filename
```