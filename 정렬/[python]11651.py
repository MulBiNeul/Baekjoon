# 좌표 정렬하기 2 - 11651

import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x, y))

arr.sort(key=lambda x: (x[1], x[0]))
for i in arr:
    print(i[0], i[1])