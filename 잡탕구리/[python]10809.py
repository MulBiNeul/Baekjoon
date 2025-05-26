import sys

# 단어 S 입력
S = sys.stdin.readline().rstrip()

# 각 알파벳이 등장하는 첫 위치 출력
for _ in range(26):
    print(S.find(chr(97 + _)), end=' ')