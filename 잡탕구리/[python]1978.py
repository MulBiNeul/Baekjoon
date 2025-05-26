# 소수 찾기 1978

import sys

prime_number_cnt = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

cnt = 0
for num in nums:
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        cnt += 1

print(cnt)