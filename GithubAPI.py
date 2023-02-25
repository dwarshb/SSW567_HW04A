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


def main():
    gitUserName = input("Enter Github Username: ")
    gitHubApi(gitUserName)


if __name__ == "__main__":
    main()
