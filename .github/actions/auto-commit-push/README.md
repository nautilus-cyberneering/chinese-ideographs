## Commit and push files Github action

Takes a JSON with a property named "move to base folder output", commits the files specified by its value and pushes the commit

Build docker image:
```
docker build -t auto-commit-push .
```

Run docker image:
```
docker run -e INPUT_FILENAMES='{..., "move to base folder output": ["/data/000001/32/000001-32.600.2.tif", "..."]}' -e INPUT_MESSAGE="commit message" auto-commit-push  
```

Run action with `act`:
```
docker image rm act-github-actions-change-image-file-format && act -j change-image-format
```
You need to remove the previous version of the docker images created by `act`.

## Links

* [`act` docs](https://github.com/nektos/act)