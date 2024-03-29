import os

try:
    token_file = open(".token_gitlab")
    token_gitlab = token_file.read()
except:
    if os.environ.get('token_gitlab') is not None:
        token_gitlab = os.environ.get('token_gitlab')
    else:
        print(".Token_gitlab not found")
        raise SystemExit

try:
    token_file = open(".token_github")
    token_github = token_file.read()
except:
    if os.environ.get('token_github') is not None:
        token_github = os.environ.get('token_github')
    else:
        print(".token_github not found")
        raise SystemExit

if os.environ.get('gitlab_username') is None:
    print("gitlab_username not found")
    raise SystemExit
else:
    gitlab_username = os.environ.get('gitlab_username')

if os.environ.get('github_username') is not None:
    github_username = os.environ.get('github_username')
else:
    github_username = gitlab_username


if os.environ.get('limit_repo') is not None:
    limit_repo = os.environ.get('limit_repo')
else:
    limit_repo = "50"

if os.environ.get('import_private_repo') is not None:
    if os.environ.get('import_private_repo') == True or os.environ.get('import_private_repo') == "True" or os.environ.get('import_private_repo') == "yes":
        import_private_repo = True
else:
    import_private_repo = False

gitlab_url = f"https://gitlab.com/api/v4/projects/?owned=true&per_page={limit_repo}"
github_url = "https://api.github.com/user/repos"
