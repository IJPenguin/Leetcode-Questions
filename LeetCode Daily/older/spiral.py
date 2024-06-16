# def fill_rows(output, dim, iterVal, row, reverse):
#     val = iterVal
#     if not reverse:
#         for i in range(dim):
#             output[row][i] = val
#             val += 1
#     else:
#         for i in range(dim-1, -1, -1):
#             output[row][i] = val
#             val += 1

# def fill_columns(output, dim, iterVal, col, reverse):
#     val = iterVal
#     if not reverse:
#         for i in range(dim):
#             output[i][col] = val
#             val += 1
#     else:
#         for i in range(dim-1, -1, -1):
#             output[i][col] = val
#             val += 1


# n = 5
# output = [[0 for j in range(n)] for i in range(n)]
# reverse = False
# val = 1
# for i in range(1, 2*n):
#     if i % 2 == 1:
#         fill_rows(output, n, val, i-1, reverse)
#         val += n-1
#     else:
#         fill_columns(output, n, val, i-1, reverse)
#         reverse = not reverse
    
# print(output)

# if case == 1:
#                 iter = 0
#                 for i in range(0, n):
#                     output[row][i] = val
#                     val+=1
#                     iter+=1
#                 col = iter
#                 case = 2    
#             elif case == 2:
#                 iter = 0
#                 for i in range(0, n):
#                     output[i][col] = val
#                     val += 1
#                     iter += 1
#                 row = iter
#                 case = 3
#             elif case == 3
#                 iter 




# n = 5
# output = [[0 for j in range(n)] for i in range(n)]
# # print(output)
# reverse = False
# val = 1
# row = 0
# col = n-1

# while val<= n**2:
#     temp = 0
#     iterVal = n
#     reverse = False
#     if not reverse:
#         for i in range(0, iterVal):
#             print(val)
#             output[row][i] = val
#             val += 1
#             temp+= 1 
#         row = temp
#         for i in range(, iterVal):
#             print(val)
#             output[i][col] = val
#             val += 1
#         reverse = True
#         iterVal -= 1
#         col = col - temp
        
    # else:
    #     temp = 0
    #     for i in range(iterVal-1, -1, -1):
    #         print(val)
    #         output[row][i] = val
    #         val+= 1
    #         temp += 1
    #     row = n - temp
    #     print("this works")
    #     for i in range(iterVal-1, -1, -1):
    #         print(val)
    #         output[i][col] = val
    #         val += 1
    #     print("this works")
    #     col = temp
    #     reverse = False
    #     iterVal -= 1

