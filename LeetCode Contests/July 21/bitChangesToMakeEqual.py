n = 13
k = 4

def minChanges( n: int, k: int) -> int:
    if (k & n) != k:
            return -1
    differing_bits = n ^ k
    changes_needed = bin(differing_bits).count('1')

    return changes_needed

print(minChanges(n, k))