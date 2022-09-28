

try:
    token_file = open(".token_gitlab")
    token_gitlab = token_file.read()
except:
    print(".Token_gitlab not found")
    raise SystemExit

try:
    token_file = open(".token_github")
    token_github = token_file.read()
except:
    print(".Token_gitlab not found")
    raise SystemExit

gitlab_username = "babidi34"
github_username = "babidi34"
limit_repo = "50"
import_private_repo = True
gitlab_url = f"https://gitlab.com/api/v4/projects/?owned=true&per_page={limit_repo}"
github_url = "https://api.github.com/user/repos"