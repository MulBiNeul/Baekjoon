# 약수들의 합 - 9506

import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    else:
        divisor = []
        for i in range(n):
            if (n % (i+1)) == 0:
                divisor.append(i+1)
    
    if sum(divisor) - divisor[-1] == n:
        print(n, "=", end=" ")
        for i in range(len(divisor) - 2):
            print(divisor[i], end=" + ")
        print(divisor[-2])
    
    elif sum(divisor) != n:
        print(n, "is NOT perfect.")