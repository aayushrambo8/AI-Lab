rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
print("The grid is", rows, "rows by", columns, "columns.")

grid = [["+" for _ in range(columns)] for _ in range(rows)]

obstacles = int(input("Enter the number of obstacles: "))
obstaclePositions = []

for i in range(obstacles):
    print("Enter the row and column of the obstacle: ")
    obstacleRow = int(input())
    obstacleColumn = int(input())
    if obstacleRow < rows and obstacleColumn < columns:
        print("Obstacle at row", obstacleRow, "and column", obstacleColumn, "is present.")
        obstaclePositions.append([obstacleRow, obstacleColumn])
        grid[obstacleRow][obstacleColumn] = "X"

rewards = int(input("Enter the number of rewards: "))
rewardPositions = []

for i in range(rewards):
    print("Enter the row and column of the reward: ")
    rewardRow = int(input())
    rewardColumn = int(input())
    if rewardRow < rows and rewardColumn < columns:
        print("Reward at row", rewardRow, "and column", rewardColumn, "is present.")
        rewardPositions.append([rewardRow, rewardColumn])
        grid[rewardRow][rewardColumn] = "R"

penalties = int(input("Enter the number of penalty: "))
penaltyPositions = []

for i in range(penalties):
    print("Enter the row and column of the penalties: ")
    penaltyRow = int(input())
    penaltyColumn = int(input())
    if penaltyRow < rows and penaltyColumn < columns:
        print("Penalty at row", penaltyRow, "and column", penaltyColumn, "is present.")
        penaltyPositions.append([penaltyRow, penaltyColumn])
        grid[penaltyRow][penaltyColumn] = "P"

print("\nFinal grid:")
for row in grid:
    print(" ".join(row))

currentRow = int(input("Enter the current row: "))
currentColumn = int(input("Enter the current column: "))
goalRow = int(input("Enter the goal row: "))
goalColumn = int(input("Enter the goal column: "))

print("Current Position:", currentRow, currentColumn)
print("Goal Position:", goalRow, goalColumn)

pathLength = 0

while currentRow != goalRow or currentColumn != goalColumn:
    nextRow = currentRow
    nextColumn = currentColumn
    if currentRow != goalRow:
        if currentRow < goalRow:
            nextRow += 1
            print("Moving Down")
        else:
            nextRow -= 1
            print("Moving Up")
    elif currentColumn != goalColumn:
        if currentColumn < goalColumn:
            nextColumn += 1
            print("Moving Right")
        else:
            nextColumn -= 1
            print("Moving Left")
    if grid[nextRow][nextColumn] == "X":
        print("Obstacle found, moving away from it")
        nextRow = currentRow
        nextColumn = currentColumn
        if currentColumn < goalColumn and currentColumn + 1 < columns and grid[currentRow][currentColumn + 1] != "X":
            nextColumn += 1
            print("Moving Right")
        elif currentColumn > goalColumn and currentColumn - 1 >= 0 and grid[currentRow][currentColumn - 1] != "X":
            nextColumn -= 1
            print("Moving Left")
        elif currentRow < goalRow and currentRow + 1 < rows and grid[currentRow + 1][currentColumn] != "X":
            nextRow += 1
            print("Moving Down")
        elif currentRow > goalRow and currentRow - 1 >= 0 and grid[currentRow - 1][currentColumn] != "X":
            nextRow -= 1
            print("Moving Up")
        else:
            print("No path available")
            break
    grid[currentRow][currentColumn] = "="
    currentRow = nextRow
    currentColumn = nextColumn
    pathLength += 1
    if grid[currentRow][currentColumn] == "R":
        print("Reward collected.")
        grid[currentRow][currentColumn] = "+"
    elif grid[currentRow][currentColumn] == "P":
        print("Penalty Encountered.")
        grid[currentRow][currentColumn] = "+"
    print("\nCurrent grid:")
    for row in grid:
        print(" ".join(row))

print("Reached destination")
