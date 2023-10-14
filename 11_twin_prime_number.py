# Twin prime numbers within a given range:

while True:
    start = int(input("Enter a start range : "))
    end = int(input("Enter the end range : "))
    if start < 1 or end <= 1:
        print("Enter a valid start and end range !!")
        continue
    else:
        if start > end:
            start, end = end, start
        # if end
        prime_list = []
        twin_prime_list = []

        for i in range(start, end+1):
            count = 0
            for j in range(1, i+1):
                if i % j == 0:
                    count += 1
            if count == 2:
                prime_list.append(i)
        print(f'\nPrime numbers between {start} and {end} : {prime_list}')
        # for_loop end
        for num in range(1, len(prime_list)):
            if prime_list[num] - prime_list[num-1] == 2:
                twin_prime_list.append(prime_list[num-1])
                twin_prime_list.append(prime_list[num])
        # for_loop end
        break
print("Twin Prime numbers : ", end=" ")
count = 1
for item in twin_prime_list:
    if count % 2 == 0:
        print(f',{item}]', end=" ")
    else:
        print(f'[{item}', end="")
    count += 1