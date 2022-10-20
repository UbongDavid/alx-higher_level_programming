#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    Last_Digit = number % 10
else:
    Last_Digit = -number % 10

print(f'Last digit of {number} is {Last_Digit}', end=" ")

if Last_Digit > 5:
    print('and is greater than 5')
elif Last_Digit == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
