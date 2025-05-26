# 문자열 집합 - 14425

import sys

N, M = map(int, sys.stdin.readline().split())

arr_N = set(sys.stdin.readline().rstrip() for _ in range(N))
cnt = 0

for _ in range(M):
    word = sys.stdin.readline().rstrip()
    if word in arr_N:
        cnt += 1

print(cnt)