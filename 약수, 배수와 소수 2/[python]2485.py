# 가로수 - 2485

import sys

tree_num = int(sys.stdin.readline())

tree_list = []
for _ in range(tree_num):
    tree_list.append(int(sys.stdin.readline()))

# 가로수 간 간격 리스트
interval_list = []
for i in range(1, tree_num):
    interval_list.append(tree_list[i] - tree_list[i-1])

# 가로수 간 간격의 최대공약수
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcd_value = interval_list[0]
for i in range(1, len(interval_list)):
    gcd_value = gcd(gcd_value, interval_list[i])

# 가로수 간 간격의 최대공약수로 나누어 떨어지는 가로수 개수
def count_trees(gcd_value, interval_list):
    count = 0
    for interval in interval_list:
        count += (interval // gcd_value) - 1
    return count

result = count_trees(gcd_value, interval_list)
print(result)