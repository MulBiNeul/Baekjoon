# 덱 2 - 28279

import sys
from collections import deque

input = sys.stdin.readline
command_num = int(input())

dq = deque()
for _ in range(command_num):
    command = input().split()
    if command[0] == '1':
        dq.appendleft(command[1])
    elif command[0] == '2':
        dq.append(command[1])
    elif command[0] == '3':
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif command[0] == '4':
        if not dq:
            print(-1)
        else:
            print(dq.pop())
    elif command[0] == '5':
        print(len(dq))
    elif command[0] == '6':
        if not dq:
            print(1)
        else:
            print(0)
    elif command[0] == '7':
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif command[0] == '8':
        if not dq:
            print(-1)
        else:
            print(dq[-1])