# 소인수분해 - 11653

import sys

num = int(sys.stdin.readline())

unit = 2
while num > 1:
    while True:
        if num % unit == 0:
            print(unit)
            num = num // unit
        else:
            break
    unit += 1