# 최소공배수 - 1934

import sys

def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

num = int(sys.stdin.readline())

for _ in range(num):
    a, b = map(int, sys.stdin.readline().split())
    lcm = (a * b) // gcd(a, b)
    print(lcm)