import sys

num = int(sys.stdin.readline()) # 색종이의 개수

# 도화지 초기화
paper = [[0] * 100 for _ in range(100)]

for _ in range(num):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

result = 0
for i in range(100):
    result += paper[i].count(1)

print(result)