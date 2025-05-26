# 약수 구하기 - 2501

import sys

p, q = map(int, sys.stdin.readline().split())

arr = []
for i in range(p):
    if p % (i+1) == 0:
        arr.append(i+1)

if len(arr) < q:
    print(0)
else:
    print(arr[q-1])