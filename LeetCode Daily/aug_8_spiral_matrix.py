rows = 5
cols = 6
rStart = 1
cStart = 4

right = cStart
left = cStart
up = rStart
down = rStart

visited = []

def checker(curR, curC, visited, direction):
    global right, left, up, down

    if len(visited) >= rows * cols:
        return -1

    visited.append([curR, curC])

    if direction == 0:
        # East
        if curC >= right:
            direction = 1
            right += 1
    elif direction == 1:
        # South
        if curR >= down:
            direction = 2
            down += 1
    elif direction == 2:
        # West
        if curC <= left:
            direction = 3
            left -= 1
    elif direction == 3:
        # North
        if curR <= up:
            direction = 0
            up -= 1
    return direction

def spiral_matrix(rStart, cStart, direction):
    global right, left, up, down

    if len(visited) >= rows * cols:
        return

    direction = checker(rStart, cStart, visited, direction)

    if direction == 0:  # East
        if cStart + 1 < cols and [rStart, cStart + 1] not in visited:
            spiral_matrix(rStart, cStart + 1, direction)
        else:
            spiral_matrix(rStart + 1, cStart, (direction + 1) % 4)
    elif direction == 1:  # South
        if rStart + 1 < rows and [rStart + 1, cStart] not in visited:
            spiral_matrix(rStart + 1, cStart, direction)
        else:
            spiral_matrix(rStart, cStart - 1, (direction + 1) % 4)
    elif direction == 2:  # West
        if cStart - 1 >= 0 and [rStart, cStart - 1] not in visited:
            spiral_matrix(rStart, cStart - 1, direction)
        else:
            spiral_matrix(rStart - 1, cStart, (direction + 1) % 4)
    elif direction == 3:  # North
        if rStart - 1 >= 0 and [rStart - 1, cStart] not in visited:
            spiral_matrix(rStart - 1, cStart, direction)
        else:
            spiral_matrix(rStart, cStart + 1, (direction + 1) % 4)

spiral_matrix(rStart, cStart, 0)
print(visited)
