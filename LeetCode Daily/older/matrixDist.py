mat = [[0,0,0],[0,1,0],[1,1,1]]
res = mat


def dfs(x, y, count):
    if x < 0 or y < 0 or x >= len(mat) or y >= len(mat[0]):
        return
    
    if mat[x][y] == 0:
        return count
    
    minm = min(dfs(x + 1, y, count + 1), dfs(x - 1, y, count + 1), dfs(x, y + 1, count + 1), dfs(x, y - 1, count + 1))
    return minm
        

for i in range(len(mat)):
    for j in range(len(mat[0])):
        res[i][j] = dfs(i, j, 0)

print(res)


