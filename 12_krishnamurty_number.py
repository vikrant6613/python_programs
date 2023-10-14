# Check if a number is a Krishnamurthy Number or not :
# A Krishnamurthy number is a number whose sum of the factorial of digits is equal to the number itself.

while True:
    num = input("Enter a number :  ")
    if int(num) <= 0:
        print("Enter a valid integer number : ")
        continue
    else:
        temp_num = int(num)
        sum = 0
        while temp_num != 0:
            temp = temp_num % 10
            fact = 1
            for j in range(1, temp+1):
                fact = fact * j
            sum = sum + fact
            temp_num = temp_num // 10

    if int(num) == sum:
        print(f'{num} is krishnamurthy number.')
    else:
        print("Its not a Krishnamurthy number")
    break



