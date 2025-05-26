# 붙임성 좋은 총총이 - 26069

import sys

line = int(sys.stdin.readline())

dance = set()
for i in range(line):
    A, B = map(str, sys.stdin.readline().split())
    if A == 'ChongChong' or B == 'ChongChong':
        dance.add(A)
        dance.add(B)
    else:
        if A in dance or B in dance:
            dance.add(A)
            dance.add(B)
print(len(dance))