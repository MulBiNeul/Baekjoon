# 소수 - 2581

import sys

M, N = int(sys.stdin.readline()), int(sys.stdin.readline())

prime_list = []
flag = 0
for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        prime_list.append(i)
        flag = 1

if flag == 1:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print(-1)