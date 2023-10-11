# Python Program to Find Sum of Array

# import array as arr
from array import *

# num_arr = arr.array('i', [1.2.3])
num_arr = array('i', [])

arr_len = int(input("Enter the length of the array : "))

for i in range(arr_len):
    while True:
        num = input(f'Enter a number at {i+1} position :')
        if num.isnumeric() and int(num) > 0:
            num_arr.append(int(num))
            break
        else:
            print("Please enter a positive integer value : ")
            continue
arr_sum = 0
print("\nBelow is the array of number :")
for i in num_arr:
    arr_sum = arr_sum + i
    print(i, end=" ")

print(f'\nThe sum of the array is : {arr_sum}')
