nums = [4, 5, 0, -2, -3, 1]
k = 5

map = {0: 1}
prefix_sum = 0
count = 0

for i, num in enumerate(nums):
    prefix_sum += num
    remainder = prefix_sum % k
    # print(i, remainder)
    if remainder < 0:
        remainder += k
    if remainder in map:
        count += map[remainder]
        print(count, remainder)
        map[remainder] += 1
    else:
        map[remainder] = 1
print(map)
# print(count)