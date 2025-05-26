# 다음 소수 - 4134

import sys

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

test_case_num = int(sys.stdin.readline())

for _ in range(test_case_num):
    n = int(sys.stdin.readline())
    next_prime = n
    while True:
        if is_prime(next_prime):
            print(next_prime)
            break
        next_prime += 1