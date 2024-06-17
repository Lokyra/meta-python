my_d = [{1: 'Test', 'Name': 'Loki'}]
menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}
#print(my_d['Name'], '\n')

#my_d[2] = 'Test 2'
#my_d['Name'] = 'Thor'

#del my_d[1]

for d in my_d:
    for key, value in d.items():
        if key == "Name":
            print(str(key) + " : " + value)

