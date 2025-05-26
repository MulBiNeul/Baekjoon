# 스택 2 - 28278

import sys

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
        self.top = -1
    
    def isempty(self):
        if self.top == -1:
            return 1
        else:
            return 0

    def push(self, x):
        self.stack.append(x)
        self.size += 1
        self.top += 1
    
    def pop(self):
        if self.top == -1:
            return -1
        else:
            self.size -= 1
            self.top -= 1
            return self.stack.pop()
    
    def print(self):
        if self.top == -1:
            return -1
        else:
            return self.stack[self.top]
        
order_num = int(sys.stdin.readline())

stack = Stack()
for _ in range(order_num):
    command = sys.stdin.readline().split()
    if command[0] == '1':
        stack.push(command[1])
    elif command[0] == '2':
        print(stack.pop())
    elif command[0] == '3':
        print(stack.size)
    elif command[0] == '4':
        print(stack.isempty())
    elif command[0] == '5':
        print(stack.print())