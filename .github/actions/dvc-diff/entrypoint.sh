#!/bin/sh

# debug
#env
echo "PREVIOUS_REF: $PREVIOUS_REF"
echo "CURRENT_REF: $CURRENT_REF"

cd $DVC_REPO_DIR
pwd

# https://github.com/iterative/dvc/issues/6720
echo "dvc diff --show-json $PREVIOUS_REF $CURRENT_REF"
DIFF=$(dvc diff --show-json $PREVIOUS_REF $CURRENT_REF)

# Debug. Force output value
#DIFF='{"added": [{"path": "data/000001/32/000001-32.600.2.tif"}], "deleted": [], "modified": [], "renamed": []}'

echo $DIFF

echo "::set-output name=diff::$DIFF"