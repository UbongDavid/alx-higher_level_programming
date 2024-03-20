#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    # If argv has only one argument, number of passed args is 0.
    num_of_args = len(argv) - 1

    if num_of_args == 0:
        print(f"{num_of_args} arguments.")
        exit()
    elif num_of_args == 1:
        print(f"{num_of_args} argument:")
    else:
        print(f"{num_of_args} arguments:")

    for arg_no in range(1, num_of_args + 1):
        print(f"{arg_no}: {argv[arg_no]}")
