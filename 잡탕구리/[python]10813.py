import sys

# N, M 입력
N, M = map(int, sys.stdin.readline().split())

# 처음 바구니에는 적혀 있는 번호와 같은 번호가 적힌 공이 들어있다
# 바구니 초기화
list = []
for _ in range(N):
    list.append(_+1)

# 공 교환 M번 수행
# 공을 바꿀 바구니 2개를 선택하고 서로 교환한다
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    # 바구니 속 공 교환
    tmp = list[i-1]
    list[i-1] = list[j-1]
    list[j-1] = tmp

# 배열 N 출력
print(*list)