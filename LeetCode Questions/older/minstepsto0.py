# nums = [1,1,4,2,3]
# x = 5

# def steps(x, op):
#     if x == 0:
#         return 1
#     if x < 0:
#         return 0
#     op += min(steps(x-nums[0], op),steps(x-nums[-1], op))
#     return op

# print(steps(x, 0))

nums = [1, 1, 4, 2, 3]
x = 5

def steps(x, nums):
    if x == 0:
        return 0  
    if x < 0 or not nums:
        return float('inf')

    left_option = 1 + steps(x - nums[0], nums[1:])

    # Option 2: Subtract from the right
    right_option = 1 + steps(x - nums[-1], nums[:-1])

    return min(left_option, right_option)

result = steps(x, nums)
if result == float('inf'):
    print("It's not possible to make x equal to 0.")
else:
    print("Minimum number of operations:", result)
