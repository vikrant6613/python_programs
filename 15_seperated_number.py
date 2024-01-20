# Write a Python program which accepts a sequence of comma-separated numbers from user
# and generate a list and a tuple with those numbers. Sample data : 3, 5, 7, 23
# Output : # List : ['3', ' 5', ' 7', ' 23'] # Tuple : ('3', ' 5', ' 7', ' 23')

num = input("Enter the numbers seperated by comma(,) : ")

num_list = num.split(",")

print(f"The list is : {num_list}")
print(f"The tuple is : {tuple(num_list)}")