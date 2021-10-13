## Image resizing GitHub action

Build docker image:
```
docker build -t image-resize .
```

Run docker image:
```
docker run -e INPUT_SOURCE_IMAGE="input.tif" -e INPUT_DESTINATION_IMAGE="output.tif" -e INPUT_WIDTH="2048" -e INPUT_HEIGHT="1024" image-resize  
```

Run action with `act`:
```
docker image rm act-github-actions-resize-image && act -j resize_with_github_action
```
You need to remove the previous version of the docker images created by `act`.

## Links

* [`act` docs](https://github.com/nektos/act)