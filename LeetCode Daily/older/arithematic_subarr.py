# nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
# l = [0,1,6,4,8,7]
# r = [4,4,9,7,9,10]
nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]

def sub_checker(arr):
    if len(arr) < 2:
        return False
    if len(arr) == 2:
        return True
    res = True
    org = arr[1] - arr[0]
    for i in range(0, len(arr) - 1):
        if arr[i+1] - arr[i] != org:
            return False
    return True


def arr_creator(nums, l, r):
    arr = nums[l: r+1]
    arr = sorted(arr)
    return arr

lr = zip(l, r)
res = []
for pair in lr:
    print(pair)
    arr = arr_creator(nums, pair[0], pair[1])
    res.append(sub_checker(arr))
print(res)