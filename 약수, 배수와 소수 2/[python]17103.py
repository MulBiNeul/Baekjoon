# 골드바흐 파티션 - 17103

import sys

primes = [True for _ in range(1000001)]
primes[0] = False
primes[1] = False
# 에라토스테네스의 체
for i in range(2, 1000001):
    if primes[i] == True:
        for j in range(i * 2, 1000001, i):
            primes[j] = False

test_cases = int(sys.stdin.readline().strip())
for _ in range(test_cases):
    n = int(sys.stdin.readline().rstrip())
    count = 0
    for i in range(2, n // 2 + 1):
        if primes[i] and primes[n - i]:
            count += 1
    print(count)