from collections import defaultdict

# nums = [1, 2, 1, 1, 3]
# k = 2

# nums = [1, 2, 3, 4, 5, 1]
# k = 0


nums = [5, 4]
k = 1


def get_key_from_value(d, val):
    for key, value in d.items():
        if value == val:
            return key
    return None


d = defaultdict(int)
for num in nums:
    d[num] += 1

s = sorted(d.values(), reverse=True)
temp = s[:k]
change = 0
accepted = []
for num in temp:
    accepted.append(get_key_from_value(d, num))
res = []
prev = 0
for i, num in enumerate(nums):
    if change <= k:
        if num in accepted:
            if not res:
                res.append(num)
                prev = num
            else:
                if num != prev:
                    res.append(num)
                    prev = num
                    change += 1
                elif num == prev:
                    res.append(num)

print(len(res))