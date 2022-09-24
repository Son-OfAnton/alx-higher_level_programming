#!/usr/bin/python3
"""
Takes emaail address and URL and sends
POST request to the URL passed as an
argument and displays the body response
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    res = requests.post(url, email)
    print(res.text)
