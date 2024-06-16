nums = [0,1,1,1,0,1,1,0,1]

if nums.count(1) == len(nums):
    nums.pop(0)
    print(nums)

count = []
arr = []

def count1(arr):
    for el in arr:
        
    pass

for i, num in enumerate(nums):
    temp = nums
    if num == 0:
        temp.pop(i)
        #count largest series of 1s in temp
        #save the value
        #save the array