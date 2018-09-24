import json
import requests

def gitHubStuff(userID):
    try:
        urlString = "https://api.github.com/users/" + userID + "/repos"
    except TypeError as error:
        return "userID should be a string"
    repoList = []
    gitInfo = requests.get(urlString)
    gitJSON = json.loads(gitCommits.content.decode('utf - 8'))
    for repo in gitJSON:
        gitCommits = requests.get("https://api.github.com/users/" + userID + "/" + repo['name'] + "/commits")
        gitJSON = json.loads(gitCommits.content.decode('utf-8'))
        ref = 0
        for commitItem in gitJSON:
            ref += 1
        resultList.append([repo['name'], count])
    return resultList
