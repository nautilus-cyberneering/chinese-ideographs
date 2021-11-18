# Gold Images

A Gold image is an HQ Image generated from the raw acquired, with no further processing but cropping, aligning and, some small resizing.

## Adding a new gold image

1. Add the image to the corresponding folder.  

    ```text
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

    ```text
    dvc add --glob data/**/*.tif
    ```

    That should create a new file (dvc pointer):

    ```text
    data/000001/32/YOUR_GOLD_IMAGE.tif.dvc
    ```

    The content should be something like this:

    ```text
    outs:
    - md5: a6e3d9ac974e40a44621121962c22505
      size: 4830960
      path: 000001-32.600.2.tif
    ```

3. Push the new file to the DVC remote storage

    ```text
    export AZURE_STORAGE_ACCOUNT='...'
    export AZURE_STORAGE_KEY='...'
    dvc push
    ```

4. Add the new changes to git.

    You should have two new files in your repo:

    ```text
    new file:   data/000001/32/.gitignore
    new file:   data/000001/32/000001-32.600.2.tif.dvc
    ```

    You can commit and push those new files.

## Updating a gold image

<https://dvc.org/doc/user-guide/how-to/update-tracked-data#replacing-files>

1. Remove current file:

    ```text
    dvc remove data/000001/32/000001-32.600.2.tif.dvc
    ```

2. Copy new version and add it to dvc:

    ```text
    dvc add data/000001/32/000001-32.600.2.tif
    ```

    You have to change something on the image. Otherwise, `dvc` will not create the new .dvc file.

3. Commit changes with git

## Creating a PR to add or update gold images

You should always create a pull request for a single Gold Image when you want to add or update them.

1. Create a new issue

    The name of the new issue should follow base [issue naming conventions](../CONTRIBUTING.md) in addition to the ones described here.

    * Title: `New Gold Image: 000001-32.600.2.tif` or `Update Gold Image: 000001-32.600.2.tif`
    * Description: whatever you consider important. For example, why you are updating the image.

2. Create a new branch

    The branch name should also follow base [branch naming conventions](../CONTRIBUTING.md) in addition to the ones described here.

    Add a Gold Image:

    ```text
    git checkout -b issue-XX-add-gold-image-000001-32.600.2.tif
    ```

    Update a Gold Image:

    ```text
    git checkout -b issue-XX-update-gold-image-image-000001-32.600.2.tif
    ```

3. Add or update the image using `dvc`.

    Follow the steps in "Adding-a-gold-image" or "Updatting-a-gold-image" sections.

4. Commit your changes to the remote branch

    Commit format,

    Add a Gold Image:

    ```text
    git commit -m "[#XX]" Add Gold Image: 000001-32.600.2.tif"
    ```

    Update a Gold Image:

    ```text
    git commit -m "[#XX]" Update Gold Image: 000001-32.600.2.tif"
    ```

5. Create the pull request
