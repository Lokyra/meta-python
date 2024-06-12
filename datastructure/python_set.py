set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

#set_a.add(6)
#set_a.remove(2)

print(set_a)

print(set_a.union(set_b))
print(set_a | set_b)

print(set_a.intersection(set_b))
print(set_a & set_b)


print(set_a.difference(set_b))
print(set_a - set_b)

print(set_b.difference(set_a))
print(set_b - set_a)


print(set_b.symmetric_difference(set_a))
print(set_b ^ set_a)


