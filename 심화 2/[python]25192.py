# 인사성 밝은 곰곰이 - 25192

import sys

N = int(sys.stdin.readline())
members = set()
cnt = 0

for _ in range(N):
    member = sys.stdin.readline().strip()
    if member == 'ENTER':
        members.clear()
    elif member not in members:
        members.add(member)
        cnt += 1

print(cnt)