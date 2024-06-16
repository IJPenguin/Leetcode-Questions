grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
count = 0
for row in grid:
    for i in range(len(row)-1,-1, -1):
        if row[i] < 0:
            count += 1
            print(f"{row[i]} top")
        if row[i] > 0:
            print(f"{row[i]} bottom")
            break

print(count)