arr = [20, 16, 2, 1, 5]
# arr = [11, 1, 28, 10, 11, 15, 7]

val = 18
pairs = []
seen = []

for i in range(len(arr)):
    s = val - arr[i]
    if s in arr:
        if [arr[i], s] not in pairs and arr[i] not in seen and s not in seen:
            pairs.append([arr[i], s])
            seen.append(arr[i])
            seen.append(s)

for i in range(len(pairs)):
    if pairs[i][0] * pairs[i][1] < pairs[i][1]:
        pairs.remove(pairs[i])

print(pairs[0])
