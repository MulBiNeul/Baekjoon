# 좌표 압축 - 18870

import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

num_list_set = sorted(list(set(num_list)))
dic = {num: idx for idx, num in enumerate(num_list_set)}

for i in num_list:
    print(dic[i], end=' ')