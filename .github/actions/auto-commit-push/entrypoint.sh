#!/bin/bash


FILES=$(python $GITHUB_WORKSPACE/.github/actions/auto-commit-push/process-input.py "$FILENAMES")

git checkout $BRANCH
git pull

for file in ${FILES//,/ }
do
   echo "Commiting file: '$file'"
   git add "$file"
done

git commit -m '$MESSAGE'
git push
