#!/bin/bash

FILES=$(python $GITHUB_WORKSPACE/.github/actions/auto-commit-push/process-input.py "$FILENAMES")

git config --global user.email "githubaction@nautilus-cyberneering.de"
git config --global user.name "github action bot"

git pull

for file in ${FILES//,/ }
do
   echo "Commiting file: '$GITHUB_WORKSPACE/$file'"
   git add "$GITHUB_WORKSPACE/$file"
done

if [[ $TEST == 'TRUE' ]] 
then
   echo "git commit -m '$MESSAGE'"
   echo "git push"
else
   git commit -m '$MESSAGE'
   git push
fi