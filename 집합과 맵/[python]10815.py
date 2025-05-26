# 숫자 카드 - 10815

import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
predicted_card = list(map(int, sys.stdin.readline().split()))

card = set(card)
for i in predicted_card:
    print(1 if i in card else 0, end=' ')
