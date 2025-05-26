# 세 막대 - 14215

import sys

a, b, c = map(int, sys.stdin.readline().split())

list = [a, b, c]
list.sort()
if list[0] + list[1] <= list[2]:
    list[2] = list[0] + list[1] - 1

print(sum(list))
