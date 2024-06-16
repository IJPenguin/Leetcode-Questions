nums = [1,1,1,2,2,3]
k = 2
ans = {}
uniq = set(nums)
for num in uniq:
    ans[num] = nums.count(num)

ans = dict(sorted(ans.items(), key= lambda item: item[1], reverse=True))

counter = 0
temp = []

for key, value in ans.items():
    if counter < k:
        counter += 1
        temp.append(key)
    else:
        break

print(temp)