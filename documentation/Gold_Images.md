# Gold Images

## Adding a new gold image

1. Add the image to the corresponding folder.

```
.
├── data
│   ├── 000001
│   │   ├── 32
│   │   │   ├── 000001-32.600.2.tif
│   │   │   ├── 000001-32.600.2.tif.dvc
│   │   │   └── YOUR_GOLD_IMAGE.tif
│   │   └── 42
│   └── README.md
└── README.md
```
Make sure you follow the [conventions](./data/README.md).

2. Add the new file to `dvc`

```
dvc add --glob data/**/*.tif
```

That should create a new file (dvc pointer):
```
data/000001/32/YOUR_GOLD_IMAGE.tif.dvc
```

The content should be something like this:
```
outs:
- md5: a6e3d9ac974e40a44621121962c22505
  size: 4830960
  path: 000001-32.600.2.tif
```

3. Push the new file to the DVC remote storage

```
export AZURE_STORAGE_ACCOUNT='...'
export AZURE_STORAGE_KEY='...'
dvc push
```

4. Add the new changes to git.

You should have two new files in your repo:

```
new file:   data/000001/32/.gitignore
new file:   data/000001/32/000001-32.600.2.tif.dvc
```

You can commit and push those new files.

## Updating a gold image

https://dvc.org/doc/user-guide/how-to/update-tracked-data#replacing-files

1. Remove current file:

```
dvc remove data/000001/32/000001-32.600.2.tif.dvc
```

2. Copy new version and add it to dvc:

```
dvc add data/000001/32/000001-32.600.2.tif
```
You have to change something on the image. Otherwise, `dvc` will not create the new .dvc file.

3. Commit changes with git