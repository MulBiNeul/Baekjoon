import sys

# 스택 클래스 구현
class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, x):
        self.stack_list.append(x)
    
    def pop(self):
        return self.stack_list.pop() if self.stack_list else -1

    def size(self):
        return len(self.stack_list)

    def empty(self):
        return 1 if not self.stack_list else 0
    
    def top(self):
        return self.stack_list[-1] if self.stack_list else -1

N = int(sys.stdin.readline().strip())  # 명령 개수 입력

stack = Stack()  # 스택 객체 생성
output = []  # 출력 결과 저장 리스트

# N번 명령 입력 및 실행
for _ in range(N):
    command = sys.stdin.readline().strip().split()

    if command[0] == 'push':
        stack.push(int(command[1]))
    
    elif command[0] == 'pop':
        output.append(stack.pop())
    
    elif command[0] == 'size':
        output.append(stack.size())
    
    elif command[0] == 'empty':
        output.append(stack.empty())
    
    elif command[0] == 'top':
        output.append(stack.top())

# 결과 출력 (마지막 개행 추가)
sys.stdout.write('\n'.join(map(str, output)) + '\n')