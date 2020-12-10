#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import *

    leng = len(sys.argv)

    if leng !=  3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if sys.argv[3] == "+":
            print("{:d} + {:d} = {:d}".format(sys.argv[1], sys.argv[3],
                                              int(sys.argv[1] + int(sys.argv[3]))))
        elif sys.argv[3] == "-":
            print("{:d} - {:d} = {:d}".format(sys.argv[1], sys.argv[3],
                                              int(sys.argv[1] - int(sys.argv[3]))))
        elif sys.argv[3] == "*":
            print("{:d} * {:d} = {:d}".format(sys.argv[1], sys.argv[3],
                                              int(sys.argv[1] * int(sys.argv[3]))))
        elif sys.argv[3] == "/":
            print("{:d} / {:d} = {:d}".format(sys.argv[1], sys.argv[3],
                                              int(sys.argv[1] / int(sys.argv[3]))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit (1)
