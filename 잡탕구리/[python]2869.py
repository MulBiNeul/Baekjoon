# 달팽이는 올라가고 싶다 - 2869

import sys

day_time, night_time, height = map(int, sys.stdin.readline().split())

tmp = height - day_time
total = tmp // int((day_time - night_time) + 0.5)


left = day_time

if total*(day_time - night_time) + left >= height:
    print(total + 1)
else:
    print(total + 2)