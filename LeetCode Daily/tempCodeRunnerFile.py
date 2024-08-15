 6
rStart = 1
cStart = 4

right = cStart
left = cStart
up = rStart
down = rStart


def checker(curR, curC, visited, direction):

    if curR <= rows and curC <= cols:

        visited.append([curR, curC])

        if direction == 0:
            # east
            if curC > right:
                direction = 1
        elif direction == 1:
            # south
            if curR > down:
                direction = 2
        elif direction == 2:
            # west
            if curC > left:
                direction = 3
        elif direction == 3:
            # north
            if curR > up:
                direction = 0
        return direction
    elif len(visited) >= (rows * cols):
        return -1


visited = []


def spiral_matrix(rStart, cStart, direction):
    if direction == 0:
        # east
        direction = checker(rStart, cStart, visited, direction)
        spiral_matrix(rStart + 1, cStart, direction)

    elif direction == 1:
        # south
        direction = checker(rStart, cStart, visited, direction)
        spiral_matrix(rStart, cStart - 1, direction)
        pass
    elif direction == 2:
        # west
        direction = checker(rStart, cStart, visited, direction)
        spiral_matrix(rStart - 1, cStart, direction)
        pass
    elif direction == 3:
        # north
        direction = checker(rStart, cStart, visited, direction)
        spiral_matrix(rStart, cStart + 1, direction)
        pass
    else:
        return


spiral_matrix(rStart, cStart, 0)