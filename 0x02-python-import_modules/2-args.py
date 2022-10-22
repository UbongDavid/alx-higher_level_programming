#!/usr/bin/python3
import sys
#def main():
#   print(NumberOfArguments)

argNumMockup = ' arguments.\n'
if len(sys.argv) == 2:
    argNumMockup = ' argument.\n'
NumberOfArguments = (str(len(sys.argv) - 1) + argNumMockup)

argList = []
for i in range(len(sys.argv)):
    if i == 0:
        continue
    argItem = str(i) + ": " + sys.argv[i]
    argList.append(argItem)

ListOfArguments = "\n".join(argList)

print(NumberOfArguments + ListOfArguments)
