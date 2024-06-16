# days = 10
# meetings = [[5, 7], [1, 3], [9, 10]]

# days = 5
# meetings = [[2, 4], [1, 3]]

days = 6
meetings = [[1,6]]

# free = [1] * days

# for meeting in meetings:
#     start, end = meeting
#     for i in range(start - 1, end):
#         free[i] = 0
# print(free.count(1))

meetings.sort(key=lambda i: i[0])
r = [meetings[0]]

for start, end in meetings[1:]:
    lastEnd = r[-1][1]

    if start <= lastEnd:
        r[-1][1] = max(lastEnd, end)
    else:
        r.append([start, end])
print(r)
for start, end in r:
    days -= (end - start + 1)
print(days)