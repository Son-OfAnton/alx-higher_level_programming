#!/usr/bin/python3
"""
Takes a letter and sends a POST request
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        let = ""
    else:
        let = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    search_term = {'q': let}
    res = requests.post(url, search_term)
    try:
        res = res.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get('id'), res.get('name')))
    except ValueError:
        print("Not a valid JSON")
