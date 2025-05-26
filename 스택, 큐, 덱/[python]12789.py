# 도키도키 간식드리미 - 14789

import sys

def can_receive(arr):
    stack = []
    status = 1
    for i in arr:
        if i == status:
            status += 1
        else:
            stack.append(i)
        while stack and stack[-1] == status:
            stack.pop()
            status += 1
    if status == len(arr) + 1:
            return "Nice"
    else:
        return "Sad"

student_num = int(sys.stdin.readline())
student_arr = list(map(int, sys.stdin.readline().split()))
print(can_receive(student_arr))
