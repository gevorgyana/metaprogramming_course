#!/usr/bin/env python

import sys
def run():
    # This waits for an explicit EOF (C-D)
    # sys.stdin.read()

    # This reads all the input at once, which is exactly what I want
    x1, y1, x2, y2, x3, y3 = [int(i) for i in input().split()]
    slope_suspected_1 = (y2 - y1) / (x2 - x1)
    slope_suspected_2 = (y3 - y2) / (x3 - x2)

    if slope_suspected_1 == slope_suspected_2:
        print("The 3 points lie on the same line")
    else:
        print("The 3 points do not lie on the same line")

if __name__ == '__main__':
    run()
