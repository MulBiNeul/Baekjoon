# 약수 - 1037

import sys

N = int(sys.stdin.readline())
divisor = list(map(int, sys.stdin.readline().split()))
print(max(divisor) * min(divisor))