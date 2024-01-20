# Write a Python program to find the count of any number in a given list.

n = int(input("How many numbers do you want to enter ina list : "))
num_list =[]

for x in range(n):
    num_list.append(int(input(f"Enter the number at {x+1} position : ")))
num =int(input("Enter the number you want to search : "))

if num not in num_list:
    print(f"Number {num} is not in the list")
else:
    print(f"There are {num_list.count(num)} entries of {num} in the list")