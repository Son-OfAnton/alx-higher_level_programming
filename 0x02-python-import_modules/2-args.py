#!/usr/bin/python3
import sys

n = len(sys.argv) - 1

if n == 1:
    print("1 argument:")
elif n == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(n))
for i in range(1, n + 1):
    print("{}: {}".format(i, sys.argv[i]))
