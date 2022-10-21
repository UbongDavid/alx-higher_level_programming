def remove_char_at(str, n):
    j=0
    for i in str:
        if n == j:
            j = j+1
            continue
        else:
            print('{}'.format(i) end='')
            j = j+1
