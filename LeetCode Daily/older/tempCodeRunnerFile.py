import heapq

k = 2
w = 0
p = [1, 3, 2]
c = [0, 1, 1]

projects = list(zip(c, p))
projects.sort()

max_heap = []

index = 0

for _ in range(k):
    while index < len(projects) and projects[index][0] <= w:
        heapq.heappush(max_heap, -projects[index][1])
        index += 1

    if max_heap:
        w += -heapq.heappop(max_heap)
    else:
        break

print(w)