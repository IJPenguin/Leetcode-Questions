low = 200
high = 200
zero = 1
one = 2
count = [-5 for _ in range(high+low)]
size = 0

def check(count, size, low, high, zero, one) -> int:
    if size > high:
        return 0
    
    if count[size] != -5:
        return count[size]
    
    if size >= low:
        count[size] = check(count, (size + zero), low, high, zero , one) + check(count, (size + one), low, high, zero , one) + 1
        return count[size]
    else:
        count[size] = check(count, (size + zero), low, high, zero , one) + check(count, (size + one), low, high, zero , one)
        return count[size]
    
print(check(count, size, low, high, zero, one))