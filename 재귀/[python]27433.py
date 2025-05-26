# 팩토리얼 2 - 27433

import sys

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print((factorial(int(sys.stdin.readline()))))