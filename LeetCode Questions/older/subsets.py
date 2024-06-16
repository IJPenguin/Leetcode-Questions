nums = [4,4,4,1,4]
nums.sort()
subsets = []
subset = []

def subset_finder(i):
    if subset not in subsets:
        subsets.append(subset.copy())
    for k in range(i, len(nums)):
        if k > i and nums[k] == nums[k-1]:
            continue
        subset.append(nums[k])
        subset_finder(k+1)
        subset.pop()
        subset_finder(k+1)

subset_finder(0)
print(subsets)



def subset_finder(index, subset, subsets):
        subsets.append(subset)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            subset_finder(i+1, subset + [nums[i]], subsets)
    
        nums.sort()
        subsets = []
        subset_finder(0, [], subsets)
        return subsets
