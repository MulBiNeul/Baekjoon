cnt = int(input())
list = []

for _ in range(cnt):
    num = int(input())
    list.append(num)

list.sort()

for i in range(cnt):
    print(list[i])
