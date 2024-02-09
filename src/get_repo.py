import requests

# Get a list of all the repositories for the user
def get_all_repos():
    # Get the list of repositories
    repos = []

    # Set your GitHub personal access token
    # This is required to authenticate your request to the GitHub API
    # You can create a personal access token by following the instructions here:
    # https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
    personal_access_token = 'your-personal-access-token-here'

    # Set the headers for the request
    headers = {
        'Authorization': f'Bearer {personal_access_token}',
        'Accept': 'application/vnd.github+json',
        "X-GitHub-Api-Version": "2022-11-28"

    
}

    for index in range(1, 10000):
        url = f'https://api.github.com/users/WTFAcademy/repos?page={index}'
        response = requests.get(url, headers=headers)
        repos += response.json()

        if len(response.json()) < 30:
            break
    
    return repos

repos = get_all_repos()

# write the names into a file as json

import json

with open('repos.json', 'w') as f:
    items = []
    for repo in repos:
        username = "WTFAcademy"
        reponame = repo['name']
        repo = {'username': username, 'reponame': reponame}
        items.append(repo)
    
    json.dump(items, f)
    f.write('\n')
