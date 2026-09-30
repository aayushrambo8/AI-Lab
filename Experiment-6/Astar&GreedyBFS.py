def heuristic(row, col, goalRow, goalCol):
    return abs(row - goalRow) + abs(col - goalCol)

def printGrid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))

def copyGrid(grid):
    return [row[:] for row in grid]

def greedyAgent(grid, startRow, startCol, goalRow, goalCol, rows, columns):
    frontier = [(heuristic(startRow, startCol, goalRow, goalCol), startRow, startCol, [(startRow, startCol)], 0)]
    visited = set()
    statesExplored = 0

    while frontier:
        frontier.sort(key=lambda entry: entry[0])
        h, row, col, path, cost = frontier.pop(0)

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
                frontier.append((heuristic(newRow, newCol, goalRow, goalCol), newRow, newCol, path + [(newRow, newCol)],
                                 cost + grid[newRow][newCol]))

    return None, None, statesExplored


def aStarAgent(grid, startRow, startCol, goalRow, goalCol, rows, columns):
    frontier = [(heuristic(startRow, startCol, goalRow, goalCol), 0, startRow, startCol, [(startRow, startCol)])]
    visited = set()
    statesExplored = 0

    while frontier:
        frontier.sort(key=lambda entry: entry[0])
        f, cost, row, col, path = frontier.pop(0)

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
                newCost = cost + grid[newRow][newCol]
                frontier.append((newCost + heuristic(newRow, newCol, goalRow, goalCol), newCost, newRow, newCol,
                                 path + [(newRow, newCol)]))

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

greedyPath, greedyCost, greedyStates = greedyAgent(copyGrid(grid), startRow, startCol, goalRow, goalCol, rows, columns)
aStarPath, aStarCost, aStarStates = aStarAgent(copyGrid(grid), startRow, startCol, goalRow, goalCol, rows, columns)

print("Greedy path:", greedyPath)
print("A* path:", aStarPath)

print("\n{:<25}{:<10}{:<10}".format("Metric", "Greedy", "A*"))
print("{:<25}{:<10}{:<10}".format("Search strategy", "priority", "priority"))
print("{:<25}{:<10}{:<10}".format("Uses cell weights?", "No", "Yes"))
print("{:<25}{:<10}{:<10}".format("States explored", greedyStates, aStarStates))
print("{:<25}{:<10}{:<10}".format("Solution cost", str(greedyCost), str(aStarCost)))