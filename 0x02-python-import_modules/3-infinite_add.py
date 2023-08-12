#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if (args == 1):
        print("{}".format(args))
    else:
        args_total = 0
        for i in range(1, args + 1):
            args_total += int(sys.argv[i])
        print("{}".format(args_total))
