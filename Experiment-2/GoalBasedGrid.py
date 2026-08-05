row = int(input("Enter the number of rows in the grid: "))
column = int(input("Enter the number of columns in the grid: "))
currentRow = int(input("\nEnter the current row: "))
currentColumn = int(input("Enter the current column: "))
goalRow = int(input("\nEnter the goal row: "))
goalColumn = int(input("Enter the goal column: "))
print("\nStarting to move")
while currentRow != goalRow:
    if currentRow > goalRow:
        print("Moving up")
        currentRow -= 1
    elif currentRow < goalRow:
        print("Moving down")
        currentRow += 1
print("Reached Row")

while currentColumn != goalColumn:

    if currentColumn > goalColumn:
        print("Moving Left")
        currentColumn -= 1
    elif currentColumn < goalColumn:
        print("Moving Right")
        currentColumn += 1
print("Reached Column")

print("Reached destination")

