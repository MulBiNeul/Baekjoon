# 최소공배수 - 13241

import sys

def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

a, b = map(int, sys.stdin.readline().split())
lcm = (a * b) // gcd(a, b)
print(lcm)