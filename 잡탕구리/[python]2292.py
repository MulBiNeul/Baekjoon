# 벌집 - 2292

import sys

N = int(sys.stdin.readline())

cnt = 1
for i in range(N):
    cnt += 6 * i
    if N <= cnt:
        print(i + 1)
        break