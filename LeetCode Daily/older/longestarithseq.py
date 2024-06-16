nums = [20,1,15,3,10,5,8]   
# nums = [83,20,17,43,52,78,68,45]

dp = ["." for _ in range(len(nums))]

for i , num in enumerate(nums):
    tmp = {}
    for j in range(i):
        diff = abs(num - nums[j])
        for item in dp:
            if diff in item:
                tmp[diff] = item[diff] + 1
                dp[i] = tmp.diff
            else:
                tmp[diff] = 1
                dp[i] = tmp[diff]

print(dp)
        