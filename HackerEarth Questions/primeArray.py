import math

n = 4
arr = [1, 1, 4, 5]
# arr = [4, 5, 6, 2]

# T = int(input())

# for i in range(T):
#     n = int(input())
#     arr = list(map(int, input().strip().split()))
#     print(solve(n, arr))

def primeChecker(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True
    
def solve(n, arr):
    arr.sort()
    res = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(j, len(arr)):
                # print(i, j, k)
                # print(arr[i], arr[j], arr[k])
                num = arr[i] * arr[j] * arr[k]
                print(num, primeChecker(num))
                if primeChecker(num):
                    res += 1
    return res

print(solve(n, arr))

