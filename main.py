import fonctions

public_repo_gitlab = fonctions.get_repos_public_gitlab()
private_repo_gitlab = fonctions.get_repos_private_gitlab()
repos_github = fonctions.get_repos_github()
fonctions.create_repo_github("mon_nouveau_repo_de_test")

print(repos_github)


