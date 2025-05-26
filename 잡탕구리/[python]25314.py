import sys

# 문제의 정수 N
N = int(sys.stdin.readline())

# N바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름 출력
long_num = N / 4

# 출력
print("long " * int(long_num) + "int")