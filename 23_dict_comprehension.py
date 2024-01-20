# dictionnary comprehension

# Without using comprehension

mydict = {}
for x in range(1, 6):
    mydict[x] = x**2

print(mydict)

#Using comprehension

newdict = {x:x**2 for x in range(1,6) if x != 3}
print(newdict)