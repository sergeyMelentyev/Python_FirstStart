# Declare a new dictionary object
dict0 = dict(name='Olga', job='Dev', age=27)
dict1 = {'name': {'first': 'Olga', 'last': 'Olga'},
         'jobs': ['dev', 'it'],
         'age': 27}
dict3 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 5}

# Check dict if key is present
if 'lastName' in dict1:
    print('Key is present')
else:
    print('Key is missing')

# Check dict if key is present else assign a new value
value = dict1['lastName'] if 'lastName' in dict1 else 'none'

# Zipping two lists in one dictionary
zipped = dict(zip(['name', 'job', 'age'], ['Sergey', 'IT', '34']))

# Sort dict by key value
for key in sorted(dict3):
    print(key, '=', dict3[key])
