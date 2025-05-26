# 나는야 포켓몬 마스터 이다솜 - 1620

import sys

poketmon_num, question_num = map(int, sys.stdin.readline().split())

num_to_name = {}
name_to_num = {}

for i in range(1, poketmon_num + 1):
    name = sys.stdin.readline().rstrip()
    num_to_name[i] = name
    name_to_num[name] = i

for _ in range(question_num):
    question = sys.stdin.readline().rstrip()
    if question.isdigit():
        print(num_to_name[int(question)])
    else:
        print(name_to_num[question])
