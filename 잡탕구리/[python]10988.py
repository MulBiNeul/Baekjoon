import sys

# 팰린드롬

# 단어 입력
word = sys.stdin.readline().rstrip()

state = 0 # 팰린드롬 상태

for _ in word:
    if word == word[::-1]:
        state = 1
    else:
        state = 0

if state == 1:
    print(1)
else:
    print(0)