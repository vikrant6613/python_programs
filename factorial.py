#Python Program to Find the Factorial of a Number

while(True):
    num = int(input("Enter any number : "))
    if num <= 0:
        print("Enter a positive number !!")
        continue
    else:
        fact_num = 1
        for i in range(1, num+1):
            fact_num = fact_num * i
        print(f'factorial of {num} is {fact_num}')
        break
# end
