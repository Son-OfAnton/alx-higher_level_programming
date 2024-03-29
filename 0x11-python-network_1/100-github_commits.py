#!/usr/bin/python3
"""
takes repo name and username then prints
10 commits
"""

import sys
import requests

if __name__ == '__main__':
    repo_name = sys.argv[1]
    user = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo_name)
    res = requests.get(url)
    response = res.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                response[i].get('sha'),
                response[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
