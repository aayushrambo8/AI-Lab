import math
import random

def printGrid (grid):
    for row in grid:
        print (" ".join (str (cell) for cell in row))

def copyGrid (grid):
    return [row[:] for row in grid]

def heuristic (row, col, goalRow, goalCol):
    return abs (row - goalRow) + abs (col - goalCol)

def hillClimbAgent (grid, startRow, startCol, goalRow, goalCol, rows, columns):
    row, col = startRow, startCol
    path = [(row, col)]
    cost = 0
    statesExplored = 1
    
    while not (row == goalRow and col == goalCol):
        bestRow, bestCol = None, None
        bestH = heuristic (row, col, goalRow, goalCol)
        
        for dRow, dCol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newRow, newCol = row + dRow, col + dCol
            if 0 <= newRow < rows and 0 <= newCol < columns and grid[newRow][newCol] != "X":
                newH = heuristic (newRow, newCol, goalRow, goalCol)
                if newH < bestH:
                    bestRow, bestCol, bestH = newRow, newCol, newH
        
        if bestRow is None:
            return path, cost, statesExplored, False
        
        row, col = bestRow, bestCol
        path.append ((row, col))
        cost += grid[row][col]
        statesExplored += 1
    
    return path, cost, statesExplored, True

def annealingAgent (grid, startRow, startCol, goalRow, goalCol, rows, columns):
    row, col = startRow, startCol
    path = [(row, col)]
    cost = 0
    statesExplored = 1
    temperature = 100.0
    coolingRate = 0.99
    
    while temperature > 0.01:
        if row == goalRow and col == goalCol:
            return path, cost, statesExplored, True
        neighbours = []
        for dRow, dCol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newRow, newCol = row + dRow, col + dCol
            if 0 <= newRow < rows and 0 <= newCol < columns and grid[newRow][newCol] != "X":
                neighbours.append ((newRow, newCol))
        if not neighbours:
            return path, cost, statesExplored, False
        newRow, newCol = random.choice (neighbours)
        delta = heuristic (row, col, goalRow, goalCol) - heuristic (newRow, newCol, goalRow, goalCol)
        if delta > 0 or random.random () < math.exp (delta / temperature):
            row, col = newRow, newCol
            path.append ((row, col))
            cost += grid[row][col]
            statesExplored += 1
        temperature *= coolingRate
    return path, cost, statesExplored, (row == goalRow and col == goalCol)

rows = int (input ("Enter the number of rows: "))
columns = int (input ("Enter the number of columns: "))
grid = [[1] * columns for _ in range (rows)]
printGrid (grid)
obstacles = int (input ("Enter the number of obstacles: "))
for _ in range (obstacles):
    row = int (input ("Obstacle row: "))
    col = int (input ("Obstacle column: "))
    grid[row][col] = "X"

weightedCells = int (input ("Enter the number of weighted cells: "))
for _ in range (weightedCells):
    row = int (input ("Weighted cell row: "))
    col = int (input ("Weighted cell column: "))
    grid[row][col] = int (input ("Weight: "))

startRow = int (input ("Enter the current row: "))
startCol = int (input ("Enter the current column: "))
goalRow = int (input ("Enter the goal row: "))
goalCol = int (input ("Enter the goal column: "))

printGrid (grid)

hillPath, hillCost, hillStates, hillReached = hillClimbAgent (copyGrid (grid), startRow, startCol, goalRow, goalCol,rows, columns)
saPath, saCost, saStates, saReached = annealingAgent (copyGrid (grid), startRow, startCol, goalRow, goalCol, rows,columns)

print ("\nHill climbing path:", hillPath)
print ("Simulated annealing path:", saPath)

print ("\n{:<25}{:<15}{:<20}".format ("Metric", "Hill Climbing", "Sim. Annealing"))
print ("{:<25}{:<15}{:<20}".format ("Search strategy", "local search", "local search"))
print ("{:<25}{:<15}{:<20}".format ("Uses cell weights?", "No", "No"))
print ("{:<25}{:<15}{:<20}".format ("Accepts worse moves?", "No", "Yes (random)"))
print ("{:<25}{:<15}{:<20}".format ("Goal reached?", "Yes" if hillReached else "No", "Yes" if saReached else "No"))
print ("{:<25}{:<15}{:<20}".format ("States explored", hillStates, saStates))
print ("{:<25}{:<15}{:<20}".format ("Solution cost", str (hillCost), str (saCost)))
