# nums = [1, 3, 5, 2]
# cost = [2, 3, 1, 14]

nums = [576257,268115,512826,523563,927189,39253,720661,35147,552624,847824,354489,760949,734966,571013]
cost = [842872,273313,503060,139143,367612,217125,271272,407727,199063,120280,819193,935689,624116,453146]
res = []


for i in range(len(nums)):
    for j in range(0, len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            cost[j], cost[j+1] = cost[j+1], cost[j]

middle_index = len(nums)//2

if len(nums) % 2 == 0:
    middle_elements = nums[middle_index - 1:middle_index + 1]
else:
    middle_elements = [nums[middle_index]]

for i in range(len(middle_elements)):
    ans = 0
    for j , num in enumerate(nums):
        if num > middle_elements[i]:
            while num > middle_elements[i]:
                num -= 1
                ans += cost[j]
        elif num < middle_elements[i]:
            while num < middle_elements[i]:
                num += 1
                ans += cost[j]
        else:
            continue
        
    res.append(ans)

print(res)

