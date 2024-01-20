# Python program to find second-largest number in a list

list_len = int(input("Enter thw length of the list: "))
num_list = []
for i in range(list_len):
    while True:
        num = input(f'Enter the number at {i+1} position : ')
        if num.isnumeric():
            num_list.append(int(num))
            break
        else:
            print("Enter a valid integer value.")
            continue

print(f'\nElements in the list : {num_list}')
print(f'Second largest number in the list is : {sorted(num_list)[-2]}')




