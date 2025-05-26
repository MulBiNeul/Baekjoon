# 서로 다른 부분 문자열의 개수 - 11478

import sys

word = sys.stdin.readline().strip()
result = set()
for i in range(len(word)):
    for j in range(i, len(word)):
        result.add(word[i:j+1])

print(len(result))