def printGrid(grid):
    for row in grid:
        print(" ".join(row))

def copyGrid(grid):
    return [row[:] for row in grid]

def unawareAgent(grid, row, col, goalRow, goalCol, rows, columns):
    path = [(row, col)]

    while row != goalRow or col != goalCol:
        newRow, newCol = row, col
        if row != goalRow:
            newRow += 1 if row < goalRow else -1
        elif col != goalCol:
            newCol += 1 if col < goalCol else -1
        if grid[newRow][newCol] == "X":
            if col != goalCol and 0 <= col + (1 if col < goalCol else -1) < columns and grid[row][
                col + (1 if col < goalCol else -1)] != "X":
                newRow, newCol = row, col + (1 if col < goalCol else -1)
            elif row != goalRow and 0 <= row + (1 if row < goalRow else -1) < rows and \
                    grid[row + (1 if row < goalRow else -1)][col] != "X":
                newRow, newCol = row + (1 if row < goalRow else -1), col
            else:
                return None
        row, col = newRow, newCol
        path.append((row, col))
    return path

def bfsAgent(grid, startRow, startCol, goalRow, goalCol, rows, columns):
    visited = [[False] * columns for _ in range(rows)]
    cellsRow = [startRow]
    cellsCol = [startCol]
    cellsDist = [0]
    visited[startRow][startCol] = True

    front = 0
    while front < len(cellsRow):
        row = cellsRow[front]
        col = cellsCol[front]
        dist = cellsDist[front]
        front += 1

        if row == goalRow and col == goalCol:
            return dist

        for dRow, dCol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newRow, newCol = row + dRow, col + dCol
            if 0 <= newRow < rows and 0 <= newCol < columns and not visited[newRow][newCol] and grid[newRow][
                newCol] != "X":
                visited[newRow][newCol] = True
                cellsRow.append(newRow)
                cellsCol.append(newCol)
                cellsDist.append(dist + 1)

    return None


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
grid = [["+"] * columns for _ in range(rows)]

obstacles = int(input("Enter the number of obstacles: "))
for _ in range(obstacles):
    row = int(input("Obstacle row: "))
    col = int(input("Obstacle column: "))
    grid[row][col] = "X"

startRow = int(input("Enter the current row: "))
startCol = int(input("Enter the current column: "))
goalRow = int(input("Enter the goal row: "))
goalCol = int(input("Enter the goal column: "))

printGrid(grid)

unawarePath = unawareAgent(copyGrid(grid), startRow, startCol, goalRow, goalCol, rows, columns)
bfsLength = bfsAgent(grid, startRow, startCol, goalRow, goalCol, rows, columns)
unawareLength = None if unawarePath is None else len(unawarePath) - 1

print("Unaware agent path length:", unawareLength)
print("BFS agent path length:", bfsLength)

unawareGrid = copyGrid(grid)
if unawarePath:
    for row, col in unawarePath:
        if unawareGrid[row][col] == "+":
            unawareGrid[row][col] = "-"

if unawareLength is None and bfsLength is None:
    print("The environment has no valid path.")
elif unawareLength is None and bfsLength is not None:
    print("The BFS agent found a valid path while the unaware agent stuck.")
elif bfsLength is None and unawareLength is not None:
    print("The unaware agent found a path while BFS did not.")
elif bfsLength < unawareLength:
    print("The BFS agent found a shorter path.")
elif unawareLength < bfsLength:
    print("The unaware agent found a shorter path.")
else:
    print("Both agents found paths of the same length.")