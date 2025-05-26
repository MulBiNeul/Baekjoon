# 알고리즘 수업 - 병합 정렬 1 - 24060

import sys

def mergeSort(lst):
    if len(lst) == 1:
        return lst

    mid = (len(lst) + 1) // 2
    # 왼쪽, 오른쪽 리스트 각각 정렬 - 재귀
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])

    lst2 = []
    i, j = 0, 0

    # 병합
    while i < len(left) and j < len(right):
        # 오름차순 정렬이므로 작은 값을 저장
        if left[i] < right[j]:
            lst2.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            lst2.append(right[j])
            ans.append(right[j])
            j += 1
    # 왼쪽 배열이 남은 경우
    while i < len(left):
        lst2.append(left[i])
        ans.append(left[i])
        i += 1
    # 오른쪽 배열이 남은 경우
    while j < len(right):
        lst2.append(right[j])
        ans.append(right[j])
        j += 1

    return lst2


N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

ans = []
mergeSort(A)

if len(ans) >= K:
    print(ans[K - 1])
else:
    print(-1)