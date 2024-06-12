my_d = {1: 'Test', 'Name': 'Loki'}

print(my_d['Name'], '\n')

my_d[2] = 'Test 2'
my_d['Name'] = 'Thor'

#del my_d[1]


for key, value in my_d.items():
    print(str(key) + " : " + value)

