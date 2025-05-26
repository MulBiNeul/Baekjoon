# 분수 합 - 1735

import sys

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
def add_fractions(A, B, C, D):
    numerator = A * D + B * C
    denominator = B * D
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

result = add_fractions(A, B, C, D)
print(result[0], result[1])