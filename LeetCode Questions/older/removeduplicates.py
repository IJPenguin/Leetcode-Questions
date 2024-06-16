nums = [0,0,1,1,1,2,2,3,3,4]
new = []
for data in nums:
    if not data in new:
        new.append(data)
        nums.remove(data)
print(new)
length = len(nums)
for data in nums:
    new.append(data)
nums = new
print(new)