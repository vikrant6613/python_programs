# Sum of the factors of the given number: input 8 : output 8 + 4 + 2 + 1 = 15

num = int(input("Enter a number : "))
i = num
fac_sum = 0
while i >= 1:
    if num % i == 0:
        fac_sum += i
    i -= 1

print("The sum of factors of {0} is {1}".format(num, fac_sum))
