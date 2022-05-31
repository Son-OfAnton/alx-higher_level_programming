#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastNum = (abs(number) % 10)
    else:
        lastNum = number % 10
    print("{}".format(lastNum), end="")
    return lastNum
