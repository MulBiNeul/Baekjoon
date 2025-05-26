# 삼각형과 세 변 - 5073

import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break
    if a == b == c:
        print("Equilateral")
    elif a >= b + c or b >= a + c or c >= a + b:
        print("Invalid")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")