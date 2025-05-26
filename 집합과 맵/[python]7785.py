# 회사에 있는 사람 - 7785

import sys

enter_num = int(sys.stdin.readline())
enter_list = set()

for _ in range(enter_num):
    name, state = sys.stdin.readline().split()
    if state == 'enter':
        enter_list.add(name)
    elif state =='leave':
        enter_list.remove(name)

enter_list = sorted(enter_list, reverse=True)

for i in enter_list:
    print(i)