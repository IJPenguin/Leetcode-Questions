# APPROACH 1

# numbers = [2,7,11,15]
numbers = [5,25,75]
target = 100

def bin_search(numbers, t, i):
    temp = []
    temp += numbers
    temp.remove(numbers[i])
    l = 0
    r = len(temp) -1 
    while l <= r:
        m = (l + r) // 2
        if temp[m] == t:
            if m < i:
                return m
            return m+1
        elif temp[m] < t:
            l = m + 1
        else: 
            r = m - 1
    return False

for i in range(len(numbers)):
    print(i)
    diff = target - numbers[i]
    a = bin_search(numbers, diff, i)
    if a:
        print([i+1, a+1])
        exit()
    
# APPROACH 2

L, R = 0, len(numbers) - 1

while L < R: 
    curSum = numbers[L] + numbers[R]
    if curSum == target: 
        print([L + 1, R + 1])
    elif curSum < target: 
        L += 1
    else: 
        R -= 1
print([-1 , -1])