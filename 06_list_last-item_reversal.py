# Python program to interchange first and last elements in a list


list_len = int(input("Enter the length of the list : "))
num_list = []
for i in range(list_len):
    num_list.append(int(input(f'Enter the element at {i+1} position : ')))

temp_list = num_list.copy()
num_list[0], num_list[-1] = num_list[-1], num_list[0]

print(f'\nOriginal List : {temp_list}')
print(f'Interchanged List : {num_list}')
