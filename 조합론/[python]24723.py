# 녹색거탑 - 24723

import sys

N = int(sys.stdin.readline())

# 1층 -> 2가지
# 2층 -> 4가지
# 3층 -> 8가지
# 4층 -> 16가지

print(2**N)