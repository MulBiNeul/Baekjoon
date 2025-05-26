# 영화감독 숌 - 1436

import sys

N = int(sys.stdin.readline())

num = 666
cnt = 0
while True:
    if '666' in str(num):
        cnt += 1
    if cnt == N:
        print(num)
        break
    num += 1