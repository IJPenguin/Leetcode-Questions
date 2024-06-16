grid = [[1],[2]]

counter = 0 

def increasingPath(grid, i, j) -> int:
    counter = 0
    try:
        if grid[i][j] < grid[i][j+1]:
            counter = 1 + increasingPath(grid,i, j+1)        
    except IndexError:
        pass

    try:
        if grid[i][j] < grid[i][j-1]:
            counter = 1 + increasingPath(grid,i, j-1)        
    except IndexError:
        pass

    try:
        if grid[i][j] < grid[i+1][j]:
            counter = 1 + increasingPath(grid,i+1, j)       
    except IndexError:
        pass

    try:
        if grid[i][j] < grid[i-1][j]:
            counter = 1 + increasingPath(grid,i-1, j)
    except IndexError:
        pass
    
    return counter

for i in range(len(grid)):
    for j in range(len(grid[i])):
        counter += 1
        counter += increasingPath(grid,i, j)

print(counter)
