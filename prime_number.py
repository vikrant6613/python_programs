# Python Program to Print all Prime numbers in an Interval
#
num_range = int(input("Enter the last number of the range : "))
num_list = []

if num_range == 0 or num_range == 1:
    print("No prime numbers in list")
else:
    for i in range(2, num_range+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count = count + 1
        if count == 2:
            num_list.append(i)
    print(f'Below are Prime numbers between 1 and {num_range}')
    for list_num in num_list:
        print(list_num)
