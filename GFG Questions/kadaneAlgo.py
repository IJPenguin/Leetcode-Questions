# arr = [1, 2, 3, -2, 5]
# arr = [-1, -2, -3, -4]
arr = [-10, -2, -3, -4]

max_sum = arr[0]
max_so_far = arr[0]

for el in arr:
    max_so_far += el
    if max_so_far > max_sum:
        max_sum = max_so_far
    if max_so_far < 0:
        max_so_far = 0


print(max_sum)
