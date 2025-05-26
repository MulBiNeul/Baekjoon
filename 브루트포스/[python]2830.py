# 설탕 배달 - 2839

import sys

N = int(sys.stdin.readline())

# 5*x + 3*y = N
arr = []
min_sum = 9999
for x in range(N//5+1):
    for y in range(N//3+1):
        if 5*x + 3*y == N:
            arr.append([x, y])
            min_sum = min(min_sum, x+y)
        
if len(arr) == 0:
    print(-1)
else:
    print(min_sum)