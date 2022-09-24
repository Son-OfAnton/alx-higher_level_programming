#!/usr/bin/python3
"""
sends a POST request to the URL passed as an
argument with the email as a parameter and
displays the body of the response
"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        response = res.read()
        print(response.decode('UTF-8'))