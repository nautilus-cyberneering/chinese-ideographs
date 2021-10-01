## DVC diff GitHub action

Build docker image:
```
docker build -t dvc-diff .
```

Run docker image:
```
docker run --rm -it dvc-diff
```

Run action with `act`:
```
docker image rm act-github-actions-dvc-diff && act -j build
```
You need to remove the previous version of the docker images created by `act`.

## Links

* [`act` docs](https://github.com/nektos/act)