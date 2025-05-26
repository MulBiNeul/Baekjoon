# 통계학 - 2108

import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

# 1. 산술평균
print(round(sum(nums) / N))

# 2. 중앙값
nums.sort()
print(nums[N // 2])

# 3. 최빈값
cnt = Counter(nums)
freq = cnt.most_common()
# 여러 개 최빈값이면 두 번째 작은 값
if len(freq) > 1 and freq[0][1] == freq[1][1]:
    print(freq[1][0])
else:
    print(freq[0][0])

# 4. 범위
print(nums[-1] - nums[0])
