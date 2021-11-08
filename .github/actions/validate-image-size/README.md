## Image validation GitHub action

Validates all the images specified by the "added" and "modified" properties in the input JSON to fit the specified bounding rectangle. The action fails if any of the images does not meet the size limits criteria.

Build docker image:
```
docker build -t image-size-validate .
```

Run docker image:
```
docker run -e JOB_STATE='{"added": [{"path": "${{ github.workspace }}/data/000001/32/000001-32.600.2.tif"}], "modified": [], "renamed": [], "not in cache": []}' -e INPUT_MIN_SIZE="1024" -e INPUT_MAX_SIZE="4096" image-size-validate  
```

Run action with `act`:
```
docker image rm act-github-actions-validate-image-size && act -j validate-size
```
You need to remove the previous version of the docker images created by `act`.

## Links

* [`act` docs](https://github.com/nektos/act)