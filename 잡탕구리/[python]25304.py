import sys

# 영수증에 적힌 총 금액 X
X = int(sys.stdin.readline())

# 영스중에 적힌 구매한 물건의 종류의 수 N
N = int(sys.stdin.readline())

# N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.
total = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    total += a * b

# 일치하면 Yes, 아니면 No
if X == total:
    print("Yes")
else:
    print("No")