## Image file format change GitHub action

Loads an image and saves it in the especified format, creating (if needed) the folder

Build docker image:
```
docker build -t change-image-format .
```

Run docker image:
```
docker run -e INPUT_JOB_STATE='{..., "icc profile modify output": ["/data/000001/32/000001-32.600.2.tif", "..."]}' -e INPUT_FORMAT="jpg" change-image-format  
```

Run action with `act`:
```
docker image rm act-github-actions-change-image-file-format && act -j change-image-format
```
You need to remove the previous version of the docker images created by `act`.

## Links

* [`act` docs](https://github.com/nektos/act)