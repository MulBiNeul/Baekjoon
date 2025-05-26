import sys

# 전공 평점 딕셔너리
major = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

total, sum = 0, 0
# 전공 평점 계산
for _ in range(20):
    subject, credit, grade = sys.stdin.readline().split()
    if grade == "P":
        continue
    else:
        sum += float(credit) * major[grade]
        total += float(credit)

print(sum / total)