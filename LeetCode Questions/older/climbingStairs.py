n = 38
memoise = {}
def backtrack(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in memoise:
        return memoise[n]
    ways = 0
    ways += backtrack(n - 1) + backtrack(n - 2)
    memoise[n] = ways

    return ways

print(backtrack(n)) 