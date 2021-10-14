#!/bin/bash

cd $DVC_REPO_DIR

echo "dvc diff --show-json $PREVIOUS_REF $CURRENT_REF"

DIFF=$(dvc diff --show-json $PREVIOUS_REF $CURRENT_REF)

ERROR=$(dvc diff --show-json $PREVIOUS_REF $CURRENT_REF 2>&1)

if [[ $DIFF == "{}" ]]; then
   DIFF='{"added": [], "deleted": [], "modified": [], "renamed": [], "not in cache": []}'
fi

# Patch for this issue: https://github.com/Nautilus-Cyberneering/chinese-ideographs/issues/38
if [[ $ERROR =~ "ERROR: unexpected error - 'not in cache'" ]]; then
   DIFF='{"added": [], "deleted": [], "modified": [], "renamed": [], "not in cache": []}'
fi

echo "::set-output name=diff::$DIFF"
echo "$DIFF"