# fibonacci series of a given number : input 8  : output 0, 1, 1, 2, 3, 5, 8, 13

num = int(input("Enter a sequence number : "))
fib_sum = 1
temp_num = 0
fib_list = []
fib_list.insert(0, 0)

for i in range(1, num):
    fib_list.append(fib_sum)
    fib_sum = fib_list[i - 1] + fib_list[i]

print(f'\nThe fibonacci series of {num} is : {fib_list}')