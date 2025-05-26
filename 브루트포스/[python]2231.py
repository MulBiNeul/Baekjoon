# 분해합 - 2231

import sys

N = int(sys.stdin.readline())

# 생성자 찾기
for i in range(1, N+1):
    num = sum(map(int, str(i))) + i
    if num == N:
        print(i)
        break
    if i == N:
        print(0)