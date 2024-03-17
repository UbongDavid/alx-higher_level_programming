#!/usr/bin/python3

def remove_char_at(string, pos):
    if pos < 0:
        pos = len(string) + pos
    new_string = ""
    for c in range(len(string)):
        if c != pos:
            new_string = new_string + string[c]
    return new_string
