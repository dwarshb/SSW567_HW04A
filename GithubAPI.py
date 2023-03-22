# Author: Darshan Bhanushali
# Homework 04a - Develop with the Perspective of the Tester in mind

import requests
import json


def gitHubApi(userid):
    results = requests.get("https://api.github.com/users/" + userid + "/repos")

    if results.status_code != 200:
        # Response when username inputted does not exist
        print("Account with this username is not present")
        return False

    response = results.json()

    # When there are no public repositories then "No Repositories" will be displayed
    if len(response) == 0:
        print("No Repositories")
        return False

    for repository in response:
        repositoryResult = requests.get(repository['commits_url'].split("{")[0])
        repositoryResult = repositoryResult.json()
        print("Repository Name: " + repository['name'] + " \n Total Number Of Commits: " + str(len(repositoryResult)))

    return True
	
def getNoOfCommits(user_id, repo_name):
    commit_url = "https://api.github.com/repos/" + user_id + "/" + repo_name + "/commits"
    commits = requests.get(commit_url)
    commits = json.loads(commits.text)
    print("Repo:", repo_name, '  Number of commits:', len(commits))
    return len(commits)
	
	

def main():
    gitUserName = input("Enter Github Username: ")
    gitHubApi(gitUserName)
    gitRepoName = input("Enter Repo Name")
    getNoOfCommits(gitUserName,gitRepoName)


if __name__ == "__main__":
    main()
