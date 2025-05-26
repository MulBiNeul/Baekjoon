# 대지 - 9063

import sys

points_num = int(sys.stdin.readline())
x_list = []
y_list = []

for _ in range(points_num):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

a = max(x_list) - min(x_list)
b = max(y_list) - min(y_list)
print(a * b)
