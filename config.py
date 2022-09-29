import os

try:
    token_file = open(".token_gitlab")
    token_gitlab = token_file.read()
except:
    try:
        token_gitlab = os.environ.get('token_gitlab')
    except:
        print(".Token_gitlab not found")
        raise SystemExit

try:
    token_file = open(".token_github")
    token_github = token_file.read()
except:
    try:
        token_github = os.environ.get('token_github')
    except:
        print(".Token_github not found")
        raise SystemExit
try:
    gitlab_username = os.environ.get('gitlab_username')
except:
    print("gitlab_username not found")
    raise SystemExit

if not os.environ.get('github_username'):
    github_username = gitlab_username
else:
    github_username = os.environ.get('github_username')

if os.environ.get('limit_repo'):
    limit_repo = os.environ.get('limit_repo')
else:
    limit_repo = "50"

if os.environ.get('import_private_repo'):
    import_private_repo = True
else:
    import_private_repo = False

gitlab_url = f"https://gitlab.com/api/v4/projects/?owned=true&per_page={limit_repo}"
github_url = "https://api.github.com/user/repos"