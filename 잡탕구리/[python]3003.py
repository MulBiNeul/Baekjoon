import sys

# 체스 말 딕셔너리 생성
chess_piece = {
    "king": 1,
    "queen": 1,
    "rook": 2,
    "bishop": 2,
    "knight": 2,
    "pawn": 8
}

# 보유 중인 체스 말 개수 입력
have_piece = list(map(int, sys.stdin.readline().split()))

# 부족하거나 많거나
for i in range(len(chess_piece)):
    print(chess_piece[list(chess_piece)[i]] - have_piece[i], end=" ")