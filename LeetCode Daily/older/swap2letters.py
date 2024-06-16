s = "ab"
goal = "ba"

if len(s) != len(goal):
    print(False)

if s == goal:
    chars = set()
    for c in s:
        if c in chars:
            print(True)
            chars.add(c)
    print(False)

diff = []
for a, b in zip(s, goal):
    if a != b:
        diff.append([a, b])
        if len(diff) > 2:
            print(False)
if len(diff) == 2 and diff[0] == diff[1][::-1]:
    print(True)
print(False)
