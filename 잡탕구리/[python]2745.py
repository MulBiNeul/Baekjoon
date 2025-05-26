# 진법 변환 - 2745

import sys

word, n = sys.stdin.readline().split()
n = int(n)
result = 0

for i in range(len(word)):
    if word[i].isalpha():
        result += (ord(word[i]) - 55) * (n ** (len(word) - i - 1))
    else:
        result += int(word[i]) * (n ** (len(word) - i - 1))

print(result)