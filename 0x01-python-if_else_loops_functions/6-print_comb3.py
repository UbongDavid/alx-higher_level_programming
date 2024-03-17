#!/usr/bin/python3
for first_digt in range(10):
    for second_digt in range(10):
        if (second_digt == 10 - 1) and (second_digt - first_digt == 1):
            print("{}{}".format(first_digt, second_digt))
        elif first_digt < second_digt:
            print("{}{}".format(first_digt, second_digt), end=', ')
