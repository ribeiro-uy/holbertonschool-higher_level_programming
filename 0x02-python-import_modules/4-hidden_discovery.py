#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    thelist = dir(hidden_4)
    for s in thelist:
        if s[0] != '_':
            print("{}".format(s))
