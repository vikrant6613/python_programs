# Python program to find sum of elements in list

list_len = int(input("Enter the length of the List : "))

num_list = []
for i in range(list_len):
    while True:
        num = input(f'Enter the element at {i+1} position : ')
        if num.isnumeric():
            num_list.append(int(num))
            break
        else:
            print("Enter a valid integer value :")
            continue
list_sum = 0
for i in num_list:
    list_sum = list_sum + i

print(f"\nElements in the list : {num_list}")
print(f'Sum of the list : {list_sum}')

