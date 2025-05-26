import sys

# N, M 입력
N, M = map(int, sys.stdin.readline().split())

# 바구니 리스트 생성
basket = [i for i in range(1, N+1)]

# 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 바꾸기
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    basket[i-1:j] = basket[i-1:j][::-1]

# 바구니 출력
print(*basket)