# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
r_height = list(reversed(height))

lwater = 0
rwater = 0

n = len(height)

if n <= 2:
    print(0)

l , r , t = 0, 1, 0

while l < len(height):
    if height[l] == 0:
        l += 1
    if l == r:
        r += 1
    present = False
    for i in range(l + 1, n):
        if height[i] >= height[l]:
            present = True
            break

    if not present: 
        l += 1
        continue

    while True:
        hl, hr = height[l], height[r]
        if hl > hr:
            lwater += hl - hr
            r += 1
        elif hl <= hr:
            l = r
            break

print(max(lwater, rwater))

