# 별 찍기 - 10 - 2447

import sys

N = int(sys.stdin.readline())

# recursive function
def star(n):
    if n == 3:
        return ['***', '* *', '***']

    arr = star(n//3)
    stars = []
    for i in arr:
        stars.append(i*3)
        for i in arr:
            stars.append(i + ' '*(n//3) + i)
    return stars

print('\n'.join(star(N)))