#!/usr/bin/python3
"""
Takes github credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    username = sys.argv[1]
    passw = sys.argv[2]

    auth = HTTPBasicAuth(username, passw)
    url = 'https://api.github.com/user'
    res = requests.get(url, auth=auth)
    print(res.json().get('id'))
