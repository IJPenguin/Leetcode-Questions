nums1 = [1,2]
nums2 = [5,4]

nums1 = sorted(nums1 + nums2)
n = len(nums1)
if n % 2 == 0:
    print((nums1[n//2] + nums1[n//2 - 1])/2)
else:
    print(nums1[n//2])