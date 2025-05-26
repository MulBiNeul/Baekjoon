# 듣보잡 - 1764

import sys

not_seen_number, not_heard_number = map(int, sys.stdin.readline().split())
not_seen = set()
not_heard = set()

for _ in range(not_seen_number):
    not_seen.add(sys.stdin.readline().rstrip())
for _ in range(not_heard_number):
    not_heard.add(sys.stdin.readline().rstrip())

not_seen_heard = sorted(list(not_seen & not_heard))
print(len(not_seen_heard))
for name in not_seen_heard:
    print(name)Z