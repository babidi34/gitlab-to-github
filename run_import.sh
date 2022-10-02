#!/bin/bash

read -p "Gitlab username : " gitlab_username

read -s -p "Gitlab token : " token_gitlab

read -s -p "Github token : " token_github

export gitlab_username=$gitlab_username
export token_gitlab=$token_gitlab
export token_github=$token_github

python3 main.py