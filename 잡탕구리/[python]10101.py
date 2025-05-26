# 삼각형 외우기 - 10101

import sys

a, b, c = int(sys.stdin.readline()), int(sys.stdin.readline()), int(sys.stdin.readline())

if a == 60 and b == 60 and c == 60:
    print("Equilateral")

elif a + b + c == 180 and (a == b or b == c or a == c):
    print("Isosceles")

elif a + b + c == 180 and (a != b and b != c and a != c):
    print("Scalene")

else:
    print("Error")