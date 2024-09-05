import time
'''
Given a sorted array of n elements, possibly with duplicates, find the number of occurrences of the target element.

Example 1:

Input: arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42], target = 8
Output: 3
Example 2:

Input: arr = [3, 5, 5, 5, 5, 7, 8, 8], target = 6
Output: 0
Example 3:

Input: arr = [3, 5, 5, 5, 5, 7, 8, 8], target = 5
Output: 4
Expected O(logn) time solution.
'''


# def findOccur(arr, target):
#     l = 0
#     r = len(arr) - 1
#     res = 0
#     while l < r:
#         mid = (l + r) // 2
#         if arr[mid] == target:
#             res += 1
#             lm = mid + 1
#             while lm <= r and arr[lm] == target:
#                 res += 1
#                 lm += 1
#             rm = mid - 1
#             while rm >= l and arr[rm] == target:
#                 res += 1
#                 rm -= 1
#             break
#         elif arr[mid] > target:
#             l = mid + 1
#         else:
#             r = mid - 1

#     return res

# def binSearch(left, right, target, arr):
#     while left < right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             if arr[mid - 1] != target:
#                 return mid
#             else:
#                 return binSearch(left, mid - 1, target, arr)
#         elif arr[mid] > target:
#             right = mid + 1
#         else:
#             left = mid - 1

# def findOccur(arr, target):
#     l = 0 
#     r = len(arr) - 1
#     res = []
#     while l < r:
#         mid = (l + r) // 2
#         if arr[mid] == target:
#             left = binSearch(l, mid, target, arr)
#             right = binSearch(mid + 1, r, target, arr)
#             return right - left + 1
#         elif arr[mid] > target:
#             l = mid + 1
#         else:
#             r = mid - 1

def binSearch(left, right, target, arr, findFirst):
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            if findFirst:
                right = mid - 1 
            else:
                left = mid + 1  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def findOccur(arr, target):
    left = binSearch(0, len(arr) - 1, target, arr, True)
    if left == -1:
        return 0  # Target not found
    right = binSearch(0, len(arr) - 1, target, arr, False)
    return right - left + 1

# arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42]
# target = 8

# arr = [1] * 1_000_000_000
# target = 1
arr = [3, 5, 5, 5, 5, 7, 8, 8]
target = 5
arr = [3, 5, 5, 5, 5, 7, 8, 8]
target = 6

print(findOccur(arr, target))
