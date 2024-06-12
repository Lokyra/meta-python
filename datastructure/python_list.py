list1 = [1,2,3,4,5]

print(*list1)
#print(list1)
print(list1, sep=" ")

list1.insert(len(list1), 6)
list1.append(7)
list1.extend([8, 9, 10])

print(list1, sep=" ")

list1.pop(4)

del list1[2]

print(list1, sep=" ")


for x in list1:
    print("Value : ", x)


