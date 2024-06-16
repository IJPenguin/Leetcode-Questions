nums = [1, 4, 3, 3, 5, 6, 3, 3, 2]
L = [1 for _ in range(len(nums))]
used = []

for i , val in enumerate(nums):
    if i in used:
        L[i] = 1
        continue
    
    if val == nums[i+1]:
        L[i] = 1
        used.append(i)
        continue

    if val > nums[i + 1]:
        pass

    if val < nums[i + 1]:
        pass
    

    used.append(i)