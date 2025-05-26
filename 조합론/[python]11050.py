# 이항 계수 1 - 11050

import sys

N, K = map(int, sys.stdin.readline().split())
# N! / (K! * (N-K)!)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
print(binomial_coefficient(N, K))