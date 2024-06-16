# n = 5
# cities = [5, 9, 10, 10, 9]
n = 10
cities = [9, 6, 8, 5, 5, 2, 8, 9, 2, 2]


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
