#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number_of_args = len(sys.argv) - 1
    if (number_of_args == 0):
        print("0 arguments.")
    elif (number_of_args == 1):
        print(number_of_args, "argument:")
        print("{}:".format(number_of_args), sys.argv[1])
    else:
        print(number_of_args, "arguments:")
        for i in range(1, number_of_args + 1):
            print("{}: {}".format(i, sys.argv[i]))
