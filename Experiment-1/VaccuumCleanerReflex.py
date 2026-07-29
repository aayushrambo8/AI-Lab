roomAStatus = int(input("Enter Room A Status "
                        "0 for dirty, 1 for clean"
                        ":"))
roomBStatus = int(input("Enter Room B Status "
                        "0 for dirty, 1 for clean"
                        ":"))
if roomAStatus == 0:
    print("Room A is Dirty.")
    print("Cleaning Room")
else:
    print("Room A is Clean.")
print("Moving to room B")
if roomBStatus == 0:
    print("Room B is Dirty.")
    print("Cleaning Room")
else:
    print("Room B is Clean.")
print("All rooms are cleaned. Shutting Down.")