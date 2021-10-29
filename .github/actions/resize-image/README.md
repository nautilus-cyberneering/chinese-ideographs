## Image resizing GitHub action

Resizes all the images specified by the "added" and "modified" properties in the input JSON to fit the specified bounding rectangle. The results are stored in the same folder, using the "-resized" suffix

Build docker image:
```
docker build -t image-resize .
```

Run docker image:
```
docker run -e INPUT_JOB_STATE='{"added": [{"path": "${{ github.workspace }}/data/000001/32/000001-32.600.2.tif"}], "modified": [], "renamed": [], "not in cache": []}' -e INPUT_WIDTH="2048" -e INPUT_HEIGHT="1024" image-resize  
```

Run action with `act`:
```
docker image rm act-github-actions-resize-image && act -j resize_with_github_action
```
You need to remove the previous version of the docker images created by `act`.

## Links

* [`act` docs](https://github.com/nektos/act)