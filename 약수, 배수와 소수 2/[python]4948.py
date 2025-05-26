import sys

# 2 * 123456 = 246912 까지 미리 소수 판별
MAX = 246912
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False

# 입력 처리
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    # n < x ≤ 2n 범위에서 소수 개수 세기
    count = sum(is_prime[n+1:2*n+1])
    print(count)