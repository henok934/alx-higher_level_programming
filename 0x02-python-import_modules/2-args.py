#!/usr/bin/python3
if __name__ == "__main__":
import sys
i = len(sys.argv) - 1
if i == 0:
    print("{} arguments.".format(i))
elif i == 1:
    print("{} argument:".format(i))
else:
    print("{} arguments:".format(i))
for argv in sys.argv:
    if i >= 1:
        i = 0
        print("{}: {}".format(i, argv))
        i = i + 1

