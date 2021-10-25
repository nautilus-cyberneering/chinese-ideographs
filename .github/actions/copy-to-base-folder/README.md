## Image file format change GitHub action

Copy base files to its destination folder

Build docker image:
```
docker build -t copy-base-image .
```

Run docker image:
```
docker run -e INPUT_STATE='{..., "file format change output": ["/data/000001/32/000001-32.600.2.tif", "..."]}' copy-base-image  
```

Run action with `act`:
```
docker image rm act-github-actions-copy-base-image && act -j copy-base-image
```
You need to remove the previous version of the docker images created by `act`.

## Links

* [`act` docs](https://github.com/nektos/act)