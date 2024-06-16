height = [1,8,6,2,5,4,8,3,7]
l , r = 0 , len(height) - 1
maxWater = []
while l < r:
    vl = height[l]
    vr = height[r]
    water = min(height[l], height[r]) * (r - l)
    maxWater.append(water)
    if vl > vr:
        r -= 1
    else:
        l += 1

print(max(maxWater))