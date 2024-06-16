nums = [-1,0,3,5,9,12]
target = 0
left = 0
right = len(nums) - 1
found = False

while not found and left <= right:
    middle = (left + right) // 2
    if target == nums[middle]:
        print(middle)
    elif target > middle:
        left = middle + 1
    else:
        right = middle - 1

if not found:
    print(-1)