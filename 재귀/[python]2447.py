# 별 찍기 - 10 - 2447

import sys

N = int(sys.stdin.readline())

# recursive function
def star(n):
    if n == 1:
        return ['*']
    stars = star(n//3)
    L = []
    for s in stars:
        L.append(s*3)
    for s in stars:
        L.append(s+ ' '*(n//3) + s)
    for s in stars:
        L.append(s*3)
    
    return L

print('\n'.join(star(N)))