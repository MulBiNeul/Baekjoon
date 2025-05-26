# 대표값2 - 2587

import sys

arr = []
for i in range(5):
    a = int(sys.stdin.readline())
    arr.append(a)

arr.sort()
print(int(sum(arr)/5))
print(arr[2])