#!/bin/bash

# https://docs.github.com/en/actions/learn-github-actions/environment-variables#default-environment-variables
echo -e "GITHUB_WORKSPACE: $GITHUB_WORKSPACE\n"
echo -e "GITHUB_SHA: $GITHUB_SHA\n"
echo -e "GITHUB_REF: $GITHUB_REF\n"
echo -e "GITHUB_HEAD_REF: $GITHUB_HEAD_REF\n"
echo -e "GITHUB_BASE_REF: $GITHUB_BASE_REF\n"
echo -e "GITHUB_EVENT_NAME: $GITHUB_EVENT_NAME\n"
echo -e "GITHUB_EVENT_PATH: $GITHUB_EVENT_PATH\n" 
#cat $GITHUB_EVENT_PATH