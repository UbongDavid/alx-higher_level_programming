#!/usr/bin/python3
for number in range(97, 123):
    if chr(number) != "q" and chr(number) != "e":
        print("{ascii_alph}".format(ascii_alph=chr(number)), end="")
