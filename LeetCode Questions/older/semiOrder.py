nums = [2,4,1,3]
n = len(nums)
iterations = 0
if nums[0] == 1 and nums[n-1] == n:
    print(iterations)
        
ind1 = nums.index(1)
        
for i in range(ind1, 0, -1):
    nums[i], nums[i-1] = nums[i-1], nums[i]
    print(nums)
    iterations += 1

indn = nums.index(n)

for i in range(indn, len(nums)-1):
    nums[i], nums[i+1] = nums[i+1], nums[i]
    print(nums)
    iterations += 1

print(f"2nd {nums}")
print(iterations)