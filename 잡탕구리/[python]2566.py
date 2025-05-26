import sys

# 9X9 행렬 입력
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

# 행렬에서의 최대값 찾기
max_val = max(map(max, matrix))

# 최대값의 위치 찾기
for i in range(9):
    for j in range(9):
        if matrix[i][j] == max_val:
            print(max_val)
            print(i + 1, j + 1)