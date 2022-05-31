#!/usr/bin/python3
revStr = ""
i = 122
while i != 96:
    if i % 2 != 0:
        revStr += chr(i - 32)
    else:
        revStr += chr(i)
    i -= 1
print("{}".format(revStr), end="")
