# 숫자 카드 2 - 10816

import sys

card_num = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))
have_card_num = int(sys.stdin.readline())
have_card_list = list(map(int, sys.stdin.readline().split()))

card_dict = {}
for card in card_list:
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1
for card in have_card_list:
    if card in card_dict:
        print(card_dict[card], end=' ')
    else:
        print(0, end=' ')