def printGrid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))


def copyGrid(grid):
    return [row[:] for row in grid]


def dfsAgent(grid, startRow, startCol, goalRow, goalCol, rows, columns):
    stack = [(startRow, startCol, [(startRow, startCol)], 0)]
    visited = set()
    statesExplored = 0

    while stack:
        row, col, path, cost = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        statesExplored += 1

        if row == goalRow and col == goalCol:
            return path, cost, statesExplored

        for dRow, dCol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newRow, newCol = row + dRow, col + dCol
            if 0 <= newRow < rows and 0 <= newCol < columns and grid[newRow][newCol] != "X" and (newRow,newCol) not in visited:
                stack.append((newRow, newCol, path + [(newRow, newCol)], cost + grid[newRow][newCol]))

    return None, None, statesExplored


def bfsAgent(grid, startRow, startCol, goalRow, goalCol, rows, columns):
    queue = [(startRow, startCol, [(startRow, startCol)], 0)]
    visited = {(startRow, startCol)}
    statesExplored = 0
    front = 0

    while front < len(queue):
        row, col, path, cost = queue[front]
        front += 1
        statesExplored += 1

        if row == goalRow and col == goalCol:
            return path, cost, statesExplored

        for dRow, dCol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newRow, newCol = row + dRow, col + dCol
            if 0 <= newRow < rows and 0 <= newCol < columns and grid[newRow][newCol] != "X" and (newRow,
                                                                                                 newCol) not in visited:
                visited.add((newRow, newCol))
                queue.append((newRow, newCol, path + [(newRow, newCol)], cost + grid[newRow][newCol]))

    return None, None, statesExplored


def ucsAgent(grid, startRow, startCol, goalRow, goalCol, rows, columns):
    frontier = [(0, startRow, startCol, [(startRow, startCol)])]
    visited = set()
    statesExplored = 0

    while frontier:
        frontier.sort(key=lambda entry: entry[0])
        cost, row, col, path = frontier.pop(0)

        if (row, col) in visited:
            continue
        visited.add((row, col))
        statesExplored += 1

        if row == goalRow and col == goalCol:
            return path, cost, statesExplored

        for dRow, dCol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newRow, newCol = row + dRow, col + dCol
            if 0 <= newRow < rows and 0 <= newCol < columns and grid[newRow][newCol] != "X" and (newRow,
                                                                                                 newCol) not in visited:
                frontier.append((cost + grid[newRow][newCol], newRow, newCol, path + [(newRow, newCol)]))

    return None, None, statesExplored


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
grid = [[1] * columns for _ in range(rows)]
printGrid(grid)
obstacles = int(input("Enter the number of obstacles: "))
for _ in range(obstacles):
    row = int(input("Obstacle row: "))
    col = int(input("Obstacle column: "))
    grid[row][col] = "X"

weightedCells = int(input("Enter the number of weighted cells: "))
for _ in range(weightedCells):
    row = int(input("Weighted cell row: "))
    col = int(input("Weighted cell column: "))
    grid[row][col] = int(input("Weight: "))

startRow = int(input("Enter the current row: "))
startCol = int(input("Enter the current column: "))
goalRow = int(input("Enter the goal row: "))
goalCol = int(input("Enter the goal column: "))

printGrid(grid)

dfsPath, dfsCost, dfsStates = dfsAgent(copyGrid(grid), startRow, startCol, goalRow, goalCol, rows, columns)
bfsPath, bfsCost, bfsStates = bfsAgent(copyGrid(grid), startRow, startCol, goalRow, goalCol, rows, columns)
ucsPath, ucsCost, ucsStates = ucsAgent(copyGrid(grid), startRow, startCol, goalRow, goalCol, rows, columns)

print("\nDFS path:", dfsPath)
print("BFS path:", bfsPath)
print("UCS path:", ucsPath)

print("\n{:<25}{:<10}{:<10}{:<10}".format("Metric", "DFS", "BFS", "UCS"))
print("{:<25}{:<10}{:<10}{:<10}".format("Search strategy", "stack", "queue", "priority"))
print("{:<25}{:<10}{:<10}{:<10}".format("Uses cell weights?", "No", "No", "Yes"))
print("{:<25}{:<10}{:<10}{:<10}".format("States explored", dfsStates, bfsStates, ucsStates))
print("{:<25}{:<10}{:<10}{:<10}".format("Solution cost", str(dfsCost), str(bfsCost), str(ucsCost)))
