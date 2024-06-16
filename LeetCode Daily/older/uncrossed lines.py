nums1 = [4, 1, 2, 5, 1, 5, 3, 4, 1, 5]
# ek random test case liya hai testing ke liye
nums2 = [3, 1, 1, 3, 2, 5, 2, 4, 1, 3, 2, 2, 5, 5, 3, 5, 5, 1, 2, 1]

# max_lines_lr = 0  # lr - left to right
# max_lines_rl = 0  # rl - right to left
# reverse = True  # for checking the list in reverse order like right to left then left to right

# # took different cases for varying sizes of the arrays
# if len(nums1) < len(nums2):
#     if reverse:
#         start_pt = 0
#         for i in range(0, len(nums1)):
#             for j in range(start_pt, len(nums2)):
#                 if nums1[i] == nums2[j]:
#                     max_lines_lr += 1
#                     start_pt = j+1
#                     break
#                 else:
#                     continue
#         reverse = False
#     else:
#         start_pt = len(nums2)
#         for i in range(len(nums1), -1, -1):
#             for j in range(start_pt, -1, -1):
#                 if nums1[i] == nums2[j]:
#                     max_lines_rl += 1
#                     start_pt = j
#                     break
#                 else:
#                     continue
# elif len(nums1) > len(nums2):
#     if reverse:
#         start_pt = 0
#         for i in range(0, len(nums2)):
#             for j in range(start_pt, len(nums1)):
#                 if nums2[i] == nums1[j]:
#                     max_lines_lr += 1
#                     start_pt = j+1
#                     break
#                 else:
#                     continue
#         reverse = False
#     else:
#         start_pt = len(nums1)
#         for i in range(len(nums2), -1, -1):
#             for j in range(start_pt, -1, -1):
#                 if nums2[i] == nums1[j]:
#                     max_lines_rl += 1
#                     start_pt = j
#                     break
#                 else:
#                     continue

# elif len(nums1) == len(nums2):  # isme chaaron tareeke se try kiya hai
#     temp_max_rl_1 = 0
#     temp_max_rl_2 = 0
#     temp_max_lr_1 = 0
#     temp_max_lr_2 = 0
#     count = 1
#     while count < 2:
#         if reverse:
#             start_pt_1 = 0
#             for i in range(0, len(nums1)):
#                 for j in range(start_pt_1, len(nums2)):
#                     if nums1[i] == nums2[j]:
#                         temp_max_lr_1 += 1
#                         start_pt_1 = j+1
#                         break
#                     else:
#                         continue

#             start_pt_2 = 0
#             for i in range(0, len(nums2)):
#                 for j in range(start_pt_2, len(nums1)):
#                     if nums2[i] == nums1[j]:
#                         temp_max_lr_2 += 1
#                         start_pt_2 = j+1
#                         break
#                     else:
#                         continue

#             if temp_max_lr_1 >= temp_max_lr_2:
#                 max_lines_lr = temp_max_lr_1
#             else:
#                 max_lines_lr = temp_max_lr_2

#             reverse = False
#         else:
#             start_pt_1 = len(nums2)-1
#             for i in range(len(nums1) - 1, -1, -1):
#                 for j in range(start_pt_1, -1, -1):
#                     if nums1[i] == nums2[j]:
#                         temp_max_rl_1 += 1
#                         start_pt_1 = j-1
#                         break
#                     else:
#                         continue

#             start_pt_2 = len(nums1) - 1
#             for i in range(len(nums2)-1, -1, -1):
#                 for j in range(start_pt_2, -1, -1):
#                     if nums2[i] == nums1[j]:
#                         temp_max_rl_2 += 1
#                         start_pt_2 = j-1
#                         break
#                     else:
#                         continue

#             if temp_max_rl_1 >= temp_max_rl_2:
#                 max_lines_rl = temp_max_rl_1
#             else:
#                 max_lines_rl = temp_max_rl_2

#             count = 3


# if max_lines_lr >= max_lines_rl:
#     print(max_lines_lr, "lr")
# else:
#     print(max_lines_rl, "rl")



dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

for i in range(1, len(nums1) + 1):
    for j in range(1, len(nums2) + 1):
        if nums1[i - 1] == nums2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp)
print(dp[- 1][-1])
