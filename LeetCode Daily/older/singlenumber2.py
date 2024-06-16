nums = [0,1,0,1,0,1,99]
snum = set(nums)
print(snum)
arr = {}
for num in snum:
    arr[num] = nums.count(num)

print(list(arr.keys())[list(arr.values()).index(min(list(arr.values())))])