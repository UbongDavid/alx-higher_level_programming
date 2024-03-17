#!/usr/bin/python3

def uppercase(str):
    # Determine offset from begining
    # Capitals = 65 to 90
    # Small = 97 to 122

    smalls_origin = 97
    capitals_origin = 65
    cap_text = ""

    for c in str:
        if not ord(c) < 97 and not ord(c) > 122:
            sma_decim = ord(c)
            frm_origin = sma_decim - smalls_origin
            cap_decim = capitals_origin + frm_origin
            cap_text = cap_text + chr(cap_decim)
        else:
            cap_text = cap_text + c
    print("{}".format(cap_text))
