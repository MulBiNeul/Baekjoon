# 괄호 - 9012

import sys

def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 'NO'
            stack.pop()
    return 'YES' if not stack else 'NO'

T = int(sys.stdin.readline())

for i in range(T):
    ch = sys.stdin.readline().strip()
    print(is_valid_parentheses(ch))