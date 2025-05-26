# 체스판 다시 칠하기 - 1018

import sys

M, N = map(int, sys.stdin.readline().split())
board = []
for _ in range(M):
    board.append(sys.stdin.readline().rstrip())

# 각 줄에 입력된 문자열을 2차원 배열로 저장
for i in range(M):
    board[i] = list(board[i])

# 8*8 크기로 자르기
min_cnt = 64
for i in range(M-7):
    for j in range(N-7):
        cnt = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'W':
                        cnt += 1
                else:
                    if board[k][l] != 'B':
                        cnt += 1
        min_cnt = min(min_cnt, cnt, 64-cnt)
print(min_cnt)