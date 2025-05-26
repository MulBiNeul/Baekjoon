# 소수 구하기 - 1929

import sys

M, N = map(int, sys.stdin.readline().split())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for i in range(M, N+1):
    if is_prime(i):
        print(i)