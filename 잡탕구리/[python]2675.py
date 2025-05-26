import sys

R = int(sys.stdin.readline())

# 각 문자를 R번 반복해 새 문자열 P 출력
for _ in range(R):
    R_time, S = sys.stdin.readline().split()
    print(''.join([i*int(R_time) for i in S]))