# Declare a new dictionary object
dict0 = dict(name='Olga', job='Dev', age=27)
dict1 = {'name': {'first': 'Olga', 'last': 'Olga'},
         'jobs': ['dev', 'it'],
         'age': 27}
dict3 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 5}
dict4 = dict([('name', 'Sergey'), ('age', 34)])                 # from tuples
dict5 = dict.fromkeys(['a', 'b'], 0)                            # from list of keys
zipped = dict(zip(['name', 'job'], ['Sergey', 'IT']))           # zipped key/value tuples
dict6 = {key: value for (key, value) in zip(['a', 'b'], [1, 2])}
dict7 = {x: y ** 2 for (x, y) in [['a', 2], ['b', 4]]}          # {'a': 4, 'b': 16}

# Operations
zipped.keys()                                                   # all keys
zipped.values()                                                 # all values
zipped.update(dict3)                                            # merge by key
list(zipped.keys())                                             # new list of keys
list(zipped.values())                                           # new list of values
list(zipped.items())                                            # new list of key/value tuples
zipped.pop('job')                                               # delete and return from a key

# Sort dict by key value
for key in sorted(dict3):
    print(key, '=', dict3[key])

# Search dict key by value
targetValue = 1
targetKey = [key for (key, value) in dict3.items() if value == targetValue]

# Search dict value by key
targetValue = dict3['a']

# Check dict if key is present
if 'lastName' in dict1:
    print('Key is present')
else:
    print('Key is missing')

# Check dict if key is present else assign a new value
value = dict1['lastName'] if 'lastName' in dict1 else 'none'
