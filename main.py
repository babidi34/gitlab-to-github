import fonctions, config

public_repo_gitlab = fonctions.get_repos_public_gitlab()
private_repo_gitlab = fonctions.get_repos_private_gitlab()
repos_github = fonctions.get_repos_github()

for repo in public_repo_gitlab:
    fonctions.create_repo_github(repo['name'])
    fonctions.cloneGitlab_and_pushGithub(repo)

if config.import_private_repo:
    for repo in private_repo_gitlab:
        fonctions.create_private_repo_github(repo['name'])
        fonctions.cloneGitlab_and_pushGithub(repo)