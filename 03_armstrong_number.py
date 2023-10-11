# Python program to check if a number is an Armstrong number without using the power function

num = (input("Enter any number : "))
num_length = len(num)
temp_num = int(num)
arm_num = 0

while(True):
    if temp_num != 0:
        sum_num = temp_num % 10
        arm_num = arm_num + sum_num**num_length
        temp_num = temp_num // 10
    else:
        break
if arm_num == int(num):
    print(f'{num} is a armstrong number')
else:
    print(f'{num} is not a armstrong number')

