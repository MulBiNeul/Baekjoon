# 나이순 정렬 - 10814

import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    arr.append((int(age), name))

arr.sort(key = lambda x: x[0])
for i in arr:
    print(i[0], i[1])