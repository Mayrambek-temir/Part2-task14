array = ['1', '2', '3', '4', '5', '6']
print(type(array))

for i in array:
    intA=int(i)
    if intA % 2 == 0:
        print(intA)
