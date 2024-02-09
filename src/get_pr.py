from time import sleep
import requests
import json
import csv

# Set the base URL for the GitHub API
api_url = 'https://api.github.com'

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

with open('repos.json', 'r') as f:
    json_data = json.load(f)

    for item in json_data:
        sleep(1)
        # Set the name of the user or organization and the repository
        # For example, if the repository is "https://github.com/my-user/my-repo",
        # the user is "my-user" and the repository is "my-repo"
        user = item['username']
        repo = item['reponame']

        sleep(1)

        with open(f"./output/{repo}.csv","w") as csvfile:

            # Create a CSV writer
            writer = csv.writer(csvfile)

            #先写入columns_name
            writer.writerow(["pr名","用户名","url","合并时间"])

            for index in range(1, 10000):
                # Get a list of all the pull requests for the repository
                prs_url = f'{api_url}/repos/{user}/{repo}/pulls?state=close&page={index}'
                response = requests.get(prs_url, headers=headers)
                prs = response.json()
            
                writer = csv.writer(csvfile)

                # Write the header row
                # writer.writerow(['User', 'Pull Request', 'Title'])

                # Iterate through the list of pull requests
                for pr in prs:
                    # Get the login of the user who created the pull request
                    login = pr['user']['login']

                    # Get the URL and title of the pull request
                    title = pr['title']
                    url = pr['html_url']
                    merged_at = pr['merged_at'] if pr['merged_at'] else '未合并'
                    

                    # Write the data to the CSV file
                    writer.writerow([title, login, url, merged_at,])
            
                if len(prs) < 30:
                    break
