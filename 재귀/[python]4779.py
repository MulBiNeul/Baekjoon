# 칸토어 집합 - 4779

import sys

def cantor(n):
    if n == 0:
        return "-"
    else:
        return cantor(n - 1) + " " * (3 ** (n - 1)) + cantor(n - 1)

# try - except 구문을 통해 EOF 처리
while True:
    try:
        n = int(sys.stdin.readline())
        print(cantor(n))
    except:
        break