# Running GitHub Actions Locally

We are using a docker image to run GitHub Actions locally: https://github.com/nektos/act

## Basic usage

Trigger a `push` event running only the `build` job:
```
act -j build
```

Trigger a `pull request` event running only the `build` job:
```
act pull_request -j build
```

> NOTE: `act` only builds your docker GitHub actions once. If you want to force a rebuild you have to remove the previously generated image with:
```
docker image rm act-github-actions-YOUR-ACTION-FOLDER-NAME
```

## Known issues

### Some folders are not copied inside the act container

Issue: https://github.com/Nautilus-Cyberneering/chinese-ideographs/issues/39

When you run `act` with a docker action, `act` will build the docker image if it does not exist.

Sometimes you can get this error:

```
ADD failed: file not found in build context or excluded by .dockerignore: stat src: file does not exist
```

That's because the folder has not been copied inside the docker container. `act` uses a `docker cp ...` command to copy your source code into the container.

We do not know why that is happening but you can fix it by renaming the folder that has not been copied, running `act` command, and then renaming it back to the original name.

### ACT run fails on M1-based MacBooks

When `act` is run in MacBooks with Apple M1 chip, it can return to the command line just after the "Planning job"

This is easily solved adding the `--container-architecture linux/amd64` option at the end of the command.
