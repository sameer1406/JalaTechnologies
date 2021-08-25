Dict = {1: 'sameer', 2: 'jordan', 3: 'james',4:'lebron',5:'kevin'}
print("before adding new value",Dict)
Dict[6]="kobe"
print("After adding new value",Dict)
Dict[2]="mohd"
print("After updating the value",Dict)
print(Dict[2])
Dict[7] = {'Nested':{'1' : 'Life', '2' : 'is Good'}}
print("Adding a Nested Key: ")
print(Dict)
print("Accessing a Nested value: ")
print(Dict[7]['Nested']['1'])
print("Printing Key values: ")
print(Dict.keys())
del Dict[2]
print("AFter  deleting Key values: ")
print(Dict)