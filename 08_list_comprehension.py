# create a list of first 20 numbers

# without using comprehension

num_list = []

for i in range(1, 21):
    num_list.append(i)
print(f"Without list comprehension : {num_list}")

# Using list comprehension

list_num = [x for x in range(1, 21)]
print(f"Using list comprehension : {list_num}")

[print(x, end=" ") for x in range(1, 21)]

import random

ranlist = [random.randint(1, 100) for _ in range(20)]
print(f"\n{ranlist}")
