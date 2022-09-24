#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
and displays infos about it
"""

import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as res:
        response = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode('UTF-8')))
