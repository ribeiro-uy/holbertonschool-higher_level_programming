#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    leng = len(sys.argv) - 1

    if leng == 0:
        print(" 0 arguments.")
    elif leng == 1:
        print("{} argument:".format(leng))
    else:
        print("{} arguments:".format(leng))
    while i <= leng:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
