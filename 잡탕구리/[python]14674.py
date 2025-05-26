# STOP USING MONEY - 14674

import sys

N, K = map(int, sys.stdin.readline().split())
game_list = []
for _ in range(N):
    i, c, h = map(int, sys.stdin.readline().split())
    preference = h / c
    game_list.append([i, c, h, preference])

# 가성비 기준 정렬
game_list.sort(key=lambda x: (-x[3], x[1], x[0]))

# 상위 K개 출력
for i in range(K):
    print(game_list[i][0])