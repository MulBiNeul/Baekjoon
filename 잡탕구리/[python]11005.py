# 진법 변환 2 - 11005

import sys

# N과 B 입력
N, B = map(int, sys.stdin.readline().split())

result = ''
while N > 0:
    remainder = N % B
    if remainder >= 10:
        result = chr(remainder + 55) + result
    else:
        result = str(remainder) + result
    N //= B

print(result)