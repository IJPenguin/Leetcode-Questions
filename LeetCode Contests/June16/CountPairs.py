from collections import defaultdict

hours = [12, 12, 30, 24, 24]
hours = [72,48,24,3]
pairs = 0

# for i, hr in enumerate(hours):
#     for j in range(i+ 1, len(hours)):
#         if  (hr + hours[j]) % 24 == 0:
#             pairs += 1

# print(pairs)

remainder_count = defaultdict(int)
count = 0

for hour in hours:
    rem = hour % 24
    complement = (24 - rem) % 24
    if complement in remainder_count:
        count += remainder_count[complement]
    remainder_count[rem] += 1

print(count)