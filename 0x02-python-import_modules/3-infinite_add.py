#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    leng = len(sys.argv) - 1
    res = 0

    while i <= leng:
        res += int(sys.argv[i])
        i += 1
    print("{}".format(res))
