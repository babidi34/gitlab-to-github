# Gitlab-to-github

Import your repositories Gitlab to github

## Usage

Create a Personal access token with read access repo : https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html

Same for Github : https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

Install pip requirements :
```
pip3 install -r requirements.txt
```
Run bash script :
```
bash run_import.sh
```

## Variables

- token_gitlab (Required)
- token_github (Required)
- gitlab_username (Required)
- github_username (default gitlab_username)
- limit_repo (default 50)
- import_private_repo (default False)

## Authors

- [Karim Baïdi](https://gitlab.com/babidi34)
- [Linux-man.fr](https://linux-man.fr)

## License

[UNLICENSE](https://choosealicense.com/licenses/unlicense/)
