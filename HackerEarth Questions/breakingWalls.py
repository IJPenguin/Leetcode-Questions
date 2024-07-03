from collections import deque

N = 1014
xs = [-1, 1, 0, 0]
ys = [0, 0, -1, 1]
sz = [[-1] * N for _ in range(N)]
mark = [[-1] * N for _ in range(N)]
c = []
cc = 0

def bad(i, j, n, m):
    return i < 0 or j < 0 or i >= n or j >= m or c[i][j] == '#'

def dfs(i, j, n, m):
    global cc
    stack = deque()
    stack.append((i, j))
    v = []
    while stack:
        ci, cj = stack.pop()
        if bad(ci, cj, n, m) or mark[ci][cj] != -1:
            continue
        mark[ci][cj] = cc
        v.append((ci, cj))
        for d in range(4):
            ni, nj = ci + xs[d], cj + ys[d]
            stack.append((ni, nj))
    return v

def main():
    global cc
    n, m = map(int, input().split())
    for _ in range(n):
        c.append(input().strip())

    ans = 0
    for i in range(n):
        for j in range(m):
            if c[i][j] != '#' and sz[i][j] == -1:
                v = dfs(i, j, n, m)
                cnt = sum(1 for x, y in v if c[x][y] == '*')
                for x, y in v:
                    sz[x][y] = cnt
                ans = max(ans, cnt)
                cc += 1

    for i in range(n):
        for j in range(m):
            if c[i][j] == '#':
                for d1 in range(4):
                    ai, aj = i + xs[d1], j + ys[d1]
                    if not bad(ai, aj, n, m):
                        for d2 in range(d1):
                            bi, bj = i + xs[d2], j + ys[d2]
                            if not bad(bi, bj, n, m) and mark[ai][aj] != mark[bi][bj]:
                                ans = max(ans, sz[ai][aj] + sz[bi][bj])

    print(ans)

if __name__ == "__main__":
    main()
