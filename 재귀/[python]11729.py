# 하노이 탑 이동 순서 - 11729

import sys

N = int(sys.stdin.readline())

# hanoi tower
def hanoi(_from, _to, _aux, n):
    if n == 1:
        print(_from, _to)
        return
    hanoi(_from, _aux, _to, n-1)
    print(_from, _to)
    hanoi(_aux, _to, _from, n-1)

print(2**N-1)
hanoi(1, 3, 2, N)
