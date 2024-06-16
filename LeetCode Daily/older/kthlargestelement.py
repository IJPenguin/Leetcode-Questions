arr = [3,2,3,1,2,4,5,5,6]
k = 4

def quickselect(arr, k):
    if k < 1 or k > len(arr):
        return None
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quickselect_recursive(arr, low, high, k):
        if low <= high:
            pivot_index = partition(arr, low, high)
            if pivot_index == k - 1:
                return arr[pivot_index]
            elif pivot_index > k - 1:
                return quickselect_recursive(arr, low, pivot_index - 1, k)
            else:
                return quickselect_recursive(arr, pivot_index + 1, high, k)
    
    return quickselect_recursive(arr, 0, len(arr) - 1, k)

maxm = quickselect(arr, k)
print(arr)
print(maxm)
