# Check whether a number is palindrome or not


num = int(input("Enter any number"))
temp_num = num
sum = 0

while temp_num > 0:
    temp = temp_num % 10
    sum = temp + (sum*10)
    temp_num = temp_num//10

if num == sum:
    print(f"{num} is a palindrome number.")
else:
    print("Its not a palindrome number")
