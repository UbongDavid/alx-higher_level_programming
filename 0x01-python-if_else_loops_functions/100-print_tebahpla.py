#!/usr/bin/python3

print_pointer = "sma"
sma_u_bound = 122
cap_u_bound = 90

for offset in range(26):
    if print_pointer == "sma":
        c_decim = sma_u_bound - offset
        print_pointer = "cap"
    else:
        c_decim = cap_u_bound - offset
        print_pointer = "sma"
    print("{}".format(chr(c_decim)), end='')
