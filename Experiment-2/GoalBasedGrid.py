row = int(input("Enter the number of rows in the grid: "))
column = int(input("Enter the number of columns in the grid: "))
currentRow = int(input("Enter the current row: "))
currentColumn = int(input("Enter the current column: "))
currentPosition = [currentRow, currentColumn]
goalRow = int(input("Enter the goal row: "))
goalColumn = int(input("Enter the goal column: "))
goalPosition = [goalRow, goalColumn]
while currentRow != goalRow:
    if currentRow > goalRow:
        print("Moving up")
        currentRow -= 1
    elif currentRow < goalRow:
        print("Moving down")
        currentRow += 1
    else:
        print("On the Same Row")

while currentColumn != goalColumn:

    if currentColumn > goalColumn:
        print("Moving Left")
        currentColumn -= 1
    elif currentColumn < goalColumn:
        print("Moving Right")
        currentColumn += 1
    else:
        print("On the Same Column")

print("Reached destination")

