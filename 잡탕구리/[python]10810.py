import sys

# N, M 입력
N, M = map(int, sys.stdin.readline().split())

# M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다.
# 각 방법은 세 정수 i j k 로 이루어져 있다.
# i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다.

# 바구니 초기화
N = [0] * N

# M번 반복
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for i in range(i-1, j):
        N[i] = k

# 출력
for _ in N:
    print(_, end=" ")