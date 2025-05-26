# 알고리즘 수업 - 점근적 표기 1 - 24313

import sys

f_a, f_b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n = int(sys.stdin.readline())

if f_a * n + f_b <= c * n and c >= f_a:
    print(1)
else:
    print(0)