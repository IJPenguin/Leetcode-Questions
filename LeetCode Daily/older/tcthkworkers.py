costs = [17,12,10,2,7,2,11,20,8]
k = 3
candidates = 4
cost = 0
for i in range(k):
    if len(costs) > candidates:
        arr = costs[:k] + costs[-k:]
        x = arr.index(min(arr))
        cost += arr[x]
        costs.remove(arr[x])
    else:
        x = costs.index(min(costs))
        cost += costs[x]
        costs.remove(costs[x])

print(cost)