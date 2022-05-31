#!/usr/bin/python3
def uppercase(str):
    i = 0
    upperStr = ""
    while i != len(str):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            upperStr += chr(ord(str[i]) - 32)
        else:
            upperStr += str[i]
        i += 1
    print("{}".format(upperStr))
