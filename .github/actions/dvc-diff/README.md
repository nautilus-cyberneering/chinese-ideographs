## DVC diff GitHub action

This action is a wrapper of the dvc diff command that

The ouput of the command is something like:

```
{"added": [], "deleted": [{"path": "data/000001/32/000001-32.600.2.tif"}], "modified": [], "renamed": [], "not in cache": []}
::set-output name=diff::{"added": [], "deleted": [{"path": "data/000001/32/000001-32.600.2.tif"}], "modified": [], "renamed": [], "not in cache": []}
```

The output variable contains the dvd diff output in json format:
```json
{
  "added": [],
  "deleted": [
    {
      "path": "data/000001/32/000001-32.600.2.tif"
    }
  ],
  "modified": [],
  "renamed": [],
  "not in cache": []
}
```

## Usage

You need to add the action in your workflow:

```yaml
- name: DVC diff
  id: dvc-diff
  uses: ./.github/actions/dvc-diff
  env:
    DVC_REPO_DIR: ${{ github.workspace }}
    PREVIOUS_REF: ${{ github.base_ref }}
    CURRENT_REF: ${{ github.head_ref }}
```

### Ouputs

| Input  | Description            |
|--------|------------------------|
| `diff` | dvc diff ouput in JSON |

## Development

Build docker image:
```
docker build -t act-github-actions-dvc-diff .
```

Run docker image:
```
docker run --rm -it \
    --env DVC_REPO_DIR="/app" \
    --env PREVIOUS_REF="" \
    --env CURRENT_REF="" \
    --volume "$(pwd):/app" --workdir "/app" act-github-actions-dvc-diff
```

Run action with `act`:
```
docker image rm act-github-actions-dvc-diff && act pull_request -j build
```
You need to remove the previous version of the docker images created by `act`.

## Links

* [`act` docs](https://github.com/nektos/act)

## Troubleshooting

There is a potencial known bug: [`diff: ERROR: unexpected error - 'not in cache'`](https://github.com/iterative/dvc/issues/6720).

Something the dvc diff command does not work as expected.

## TODO

* Should we convert env variables into action inputs? It this case it make sense becuase container is taotally couple to GitHub Action. We do not want to use the `entrypoint.sh` in other palces and we already have the ouput variable inside.