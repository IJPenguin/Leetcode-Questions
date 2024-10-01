arr = [1, 2, 4, 7, 7, 5]
# arr = [1]
arr = [1, 2, 3]


def secondLargestSmallest(arr):
    if len(arr) <= 2:
        return [-1, -1]
    largest = -1
    smallest = -1
    mx = float('-inf')
    mn = float('inf')
    for el in arr:
        if el > mx:
            largest = mx
            mx = el
        elif el > largest and el < mx:
            largest = el

        if el < mn:
            smallest = mn
            mn = el
        elif el < smallest and el > mn:
            smallest = el

    return [largest, smallest]


print(secondLargestSmallest(arr))
