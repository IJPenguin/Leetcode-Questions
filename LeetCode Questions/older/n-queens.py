n = 4

def update(unsafe, a, b):
    for i in range(n):
        for j in range(n):
            if i == a or j == b:
                if [i, j] not in unsafe:
                    unsafe.append([i, j])

    
    return unsafe

def nqueens(n):
    soln = [["." for _ in range(n)]  for _ in range(n)]
    result = []
    unsafe = []
    qcount = 0
    for i in range(n):
        for j in range(n):    
            if [i, j] not in unsafe:
                qcount += 1
                soln[i][j] = 'Q'
                unsafe = update(unsafe, i, j)  
        if qcount == n:
            result.append(soln)

    return result

print(nqueens(n))

# def is_safe(board, row, col):
#     n = len(board)

#     for i in range(col):
#         if board[row][i] == 'Q':
#             return False

#     i, j = row, col
#     while i >= 0 and j >= 0:
#         if board[i][j] == 'Q':
#             return False
#         i -= 1
#         j -= 1

#     i, j = row, col
#     while i < n and j >= 0:
#         if board[i][j] == 'Q':
#             return False
#         i += 1
#         j -= 1

#     return True

# def solve_nqueens(board, col, n, solutions):
#     if col == n:
#         solutions.append([''.join(row) for row in board])
#         return

#     for row in range(n):
#         if is_safe(board, row, col):
#             board[row][col] = 'Q'

#             solve_nqueens(board, col + 1, n, solutions)

#             board[row][col] = '.'

# def nqueens(n):
#     board = [['.' for _ in range(n)] for _ in range(n)]
#     solutions = []

#     solve_nqueens(board, 0, n, solutions)

#     return solutions

# n = 4
# print(nqueens(n))

