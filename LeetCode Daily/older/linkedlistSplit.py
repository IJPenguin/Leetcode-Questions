# arr = [1,2,3,4,5,6,7,8,9,10]
arr= [1,2,3,4,5,6,7,8,9,10]
t1 = len(arr)
k= 3
print(len(arr), k)
count = 0
res = [[] for _ in range(k)]
temp = k if len(arr) > k else 1


while len(arr) > 0:
    if not len(arr) == 1:
        for i in range(temp):
            res[count].append(arr[i])
        for i in range(temp):
            arr.pop(0)
        count += 1 
    else:
        if t1 > k:
            res[count - 1].append(arr[-1])
        else:
            res[count].append(arr[-1])
        break
    
print(res)

