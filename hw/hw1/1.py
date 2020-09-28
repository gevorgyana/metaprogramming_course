#!/usr/bin/env python

import sys
import math

def run():
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
    except IndexError:
        print("Next time, try passing the arguments. Bye..")
        exit(0)

    D = b * b - 4 * a * c
    if D > 0.0:
        D_sqrt = math.sqrt(D)
        print("x_1: {}\n x_2: {}"
              .format(D_sqrt / 2 / a, - D_sqrt / 2 / a))
    else:
        print("This equation does not have real solutions")
        exit(0)

if __name__ == '__main__':
    run()
