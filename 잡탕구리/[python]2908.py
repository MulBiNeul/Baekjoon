import sys

# 세 자리 수 두개 입력
A, B = map(int, sys.stdin.readline().split())

# 두 수를 뒤집기
A = int(str(A)[::-1])
B = int(str(B)[::-1])

if A > B:
    print(A)
else:
    print(B)