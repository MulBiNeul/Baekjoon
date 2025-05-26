# 풍성 터뜨리기 - 2346

import sys
from collections import deque

balloon_num = int(sys.stdin.readline())
order = list(map(int, sys.stdin.readline().split()))
balloon_deque = deque(enumerate(order, start=1))

while balloon_deque:
    now_balloon = balloon_deque.popleft()
    print(now_balloon[0], end=' ')
    if now_balloon[1] > 0:
        balloon_deque.rotate(-(now_balloon[1]-1))
    else:
        balloon_deque.rotate(-now_balloon[1])