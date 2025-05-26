# 영단어 암기는 괴로워 - 20920

import sys

N, M = map(int, sys.stdin.readline().split())

words = {}
# 단어장 생성
for _ in range(N):
    word = sys.stdin.readline().strip()
    if len(word) < M:
        continue
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
# 단어장 정렬
words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word in words:
    print(word[0])