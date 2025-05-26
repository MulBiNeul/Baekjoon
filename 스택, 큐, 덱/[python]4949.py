# 균형잡힌 세상 - 4949

import sys

def is_balanced(s):
    stack = []
    for char in s:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' or char == ']':
            if not stack:
                return 'no'
            elif char == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return 'no'
            elif char == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return 'no'
    return 'yes' if not stack else 'no'

while True:
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break
    print(is_balanced(s))