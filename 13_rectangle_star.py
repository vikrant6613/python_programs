# rectrangle / square hallow star program

x = int(input("Enter the length of the rectangle : "))
y = int(input("Enter the Breath of the rectangle : "))

for i in range(1, x+1):
    for j in range(1, y+1):
        if (i == 1) or (i == x) or (j == 1) or (j == y):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")