# 다리 놓기 - 1010

import sys

# 조합 공식
# nCr = n! / (n-r)! * r!
def combination(n, r):
    if r == 0 or r == n:
        return 1
    result = 1
    for i in range(1, r + 1):
        result *= n
        result //= i
        n -= 1
    return result

for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    print(combination(M, N))