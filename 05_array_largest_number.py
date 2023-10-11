# Python Program to Find Largest Element in an Array

import array as arr


num_arr = arr.array('i', [20, 30, 50, 43, 78, 39])
# print(max(num_arr))

max = num_arr[0]
for i in range(0, len(num_arr)):
    if max <= num_arr[i]:
        max = num_arr[i]
    else:
        max = max + 0
print(max)
