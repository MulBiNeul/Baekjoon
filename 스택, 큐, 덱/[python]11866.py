# 요세푸스 문제 0 - 11866

import sys
from collections import deque

def josephus(n, k):
    queue = deque([i for i in range(1, n+1)])
    result = []
    while queue:
        for _ in range(k-1):
            queue.append(queue.popleft())   # k-1번까지 뒤로 이동
        result.append(queue.popleft())      # k번째 사람 제거 후 result에 추가
    return result

input = sys.stdin.readline

n, k = map(int, input().split())
result = josephus(n, k)

print("<", end="")
print(*result, sep=", ", end="")
print(">")