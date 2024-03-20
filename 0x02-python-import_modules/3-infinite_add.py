#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    num_of_args = len(argv)
    sum = 0

    for number in range(1, num_of_args):
        sum += int(argv[number])
    print(sum)
