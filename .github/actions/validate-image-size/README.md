## Image validation GitHub action

Build docker image:
```
docker build -t image-size-validate .
```

Run docker image:
```
docker run -e INPUT_SOURCE_IMAGES="input.tif" -e INPUT_MIN_SIZE="1024" -e INPUT_MAX_SIZE="4096" image-size-validate  
```

Run action with `act`:
```
docker image rm act-github-actions-validate-image-size && act -j validate-size
```
You need to remove the previous version of the docker images created by `act`.

## Links

* [`act` docs](https://github.com/nektos/act)