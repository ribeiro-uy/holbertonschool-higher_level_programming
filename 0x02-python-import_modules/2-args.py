#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    leng = len(sys.argv) - 1

    if leng == 0:
        print(" 0 arguments.")
    elif leng == 1:
        print("{:d} argument:".format(leng))
    else:
        print("{:d} arguments:".format(leng))
    while i <= leng + 1:
        print("{:d}: {:s}".format(i, sys.argv[i]))
        i += 1
