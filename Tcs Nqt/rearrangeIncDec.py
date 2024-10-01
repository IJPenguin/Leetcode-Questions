arr = [8, 7, 1, 6, 5, 9]
# sorted = [1, 5, 6, 7, 8, 9]


def rearrangeIncDec(arr) -> list:
    arr.sort()
    n = len(arr) // 2
    return arr[:n] + arr[:n - 1:-1]


print(rearrangeIncDec(arr))
