import sys

# 다이얼 전화기
# 숫자 1을 걸려면 총 2초가 필요하므로 기본값은 2초이다
# 이후 숫자를 하나 더 누를때마다 1초씩 더 걸린다

# 다이얼 딕셔너리 생성
dial = {'A': 2, 'B': 2, 'C': 2,
        'D': 3, 'E': 3, 'F': 3,
        'G': 4, 'H': 4, 'I': 4,
        'J': 5, 'K': 5, 'L': 5,
        'M': 6, 'N': 6, 'O': 6,
        'P': 7, 'Q': 7, 'R': 7, 'S': 7,
        'T': 8, 'U': 8, 'V': 8,
        'W': 9, 'X': 9, 'Y': 9, 'Z': 9}

# 문자 입력
char = sys.stdin.readline().rstrip()

total = 0
for i in char:
    total = dial[i] + 1 + total

print(total)