
# STRIPS Based Block World

blocks = ["A", "B", "C"]

print("Initial Stack:", blocks)
print("\nSteps:")

# Remove blocks from the top and place them on the table
for i in range(len(blocks) - 1):
    print("UNSTACK", blocks[i], "from", blocks[i + 1])
    print("PUT", blocks[i], "on TABLE")

# Place blocks in reverse order
for i in range(len(blocks) - 1, 0, -1):
    print("PICKUP", blocks[i-1])
    print("STACK", blocks[i-1], "on", blocks[i])

print("\nGoal: Reverse the stack")
