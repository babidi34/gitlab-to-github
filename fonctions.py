from config import token_gitlab, token_github, gitlab_url, github_url
import requests
from requests.auth import HTTPBasicAuth
import json

def get_repos_gitlab():
    header = {"PRIVATE-TOKEN": token_gitlab}
    r = requests.get(gitlab_url,headers=header)
    return r.json()

def get_repos_public_gitlab():
    projects = get_repos_gitlab()
    repo_public = list()
    for project in projects:
        if project['visibility'] == "public":
            repo_public.append(project)
    return repo_public

def get_repos_private_gitlab():
    projects = get_repos_gitlab()
    repo_private = list()
    for project in projects:
        if project['visibility'] == "private":
            repo_private.append(project)
    return repo_private

def get_repos_github():
    request = requests.get(github_url,auth = HTTPBasicAuth('babidi34', token_github)).json()
    return request
