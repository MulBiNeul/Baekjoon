import sys

# 단어를 5개 입력 받아 리스트에 저장
words = [sys.stdin.readline().strip() for _ in range(5)]

# 출력
for i in range(15):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end='')
