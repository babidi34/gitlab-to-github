#!/bin/bash

read -p "Gitlab username : " gitlab_username

read -p "Github username : " github_username

read -s -p "Gitlab token : " token_gitlab

read -s -p "Github token : " token_github

read -p "also import private projects ? (yes or no)  : " import_private_repo

read -s -p "Max import project : (default 50) " limit_repo



export gitlab_username=$gitlab_username
export token_gitlab=$token_gitlab
export token_github=$token_github
export import_private_repo=$import_private_repo
export limit_repo=$limit_repo

python3 main.py