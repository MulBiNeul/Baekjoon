# 소트인사이드 - 1427

import sys

N = list(map(int, sys.stdin.readline().rstrip()))
N.sort(reverse=True)
for i in N:
    print(i, end='')