# 피보나치 수 5

import sys

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(int(sys.stdin.readline())))