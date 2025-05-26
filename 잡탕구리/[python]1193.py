# 분수찾기 - 1193

import sys

num = int(sys.stdin.readline())

col = num
row = 1

while col > row:
    col -= row
    row += 1

if row % 2 == 0:
    a = col
    b = row - col + 1
elif row % 2 == 1:
    a = row - col + 1
    b = col

print(f'{a}/{b}')