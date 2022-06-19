

try:
    token_file = open(".token")
    token = token_file.read()
except:
    print(".Token not found")
    raise SystemExit

gitlab_url = "https://gitlab.com/babidi34/api/v4/projects"