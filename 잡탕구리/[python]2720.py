# 세탁소 사장 동혁 - 2720

import sys

# 테스트 케이스 개수 T 입력
T = int(sys.stdin.readline())

# 테스트 케이스 개수만큼 반복
for i in range(T):
    # 거스름돈 금액 C 입력
    C = int(sys.stdin.readline())
    # 거스름돈 금액 변환
    Q = C // 25
    C %= 25
    D = C // 10
    C %= 10
    N = C // 5
    C %= 5
    P = C
    # 결과 출력
    print(Q, D, N, P)