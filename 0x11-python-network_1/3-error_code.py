#!/usr/bin/python3
"""
sends a request to the URL passed as an
argument and check for error and then,
displays the body of the response
"""

import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode('UTF-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
    except Exception:
        pass
