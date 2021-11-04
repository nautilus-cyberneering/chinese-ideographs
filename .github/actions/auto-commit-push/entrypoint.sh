#!/bin/bash

FILES=$(python app/process-input.py "$JOB_STATE")

#git config --global user.email "githubaction@nautilus-cyberneering.de"
#git config --global user.name "github action bot"

for file in ${FILES//,/ }
do
   echo "File to commit: '$GITHUB_WORKSPACE/$file'"
done
