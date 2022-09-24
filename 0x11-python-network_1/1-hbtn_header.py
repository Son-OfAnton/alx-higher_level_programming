#!/usr/bin/python3
"""
sends a request to a URL provided as an argument
and displays the value of the X-Request-Id variable
found in the header response
"""

import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        response = dict(res.headers)
        print(response.get('X-Request-Id'))
