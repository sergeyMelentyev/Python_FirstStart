# No sequences no key no mapping immutable object with unique items

x = set('spam')                                         # {'s', 'p', 'a', 'm'}
y = {'s', 'p', 'a', 'm', 'm', 'n'}                      # {'s', 'p', 'a', 'm', 'm', 'n'}

# Init an empty set and add item
z = set()
z.add('spam')                                           # {'spam'}

# Iterate over set
p = {i for i in x}                                      # {'s', 'p', 'a', 'm'}

# Insert one item
x.add('new')                                            # {'m', 's', 'a', 'new', 'p'}

# Merge
x.update({'X', 'Y'})                                    # {'m', 's', 'a', 'new', 'p', 'X', 'Y'}

# Remove
x.remove('X')                                           # {'m', 's', 'a', 'new', 'p', 'Y'}

# Working with data
engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}
a = 'bob' in engineers                                  # Is bob an engineer? True
b = engineers & managers                                # Who is both engineer and manager? 'sue'
c = engineers | managers                                # All people in either category.
d = engineers - managers                                # Engineers who are not managers. 'bob', 'ann', 'vic'
e = managers - engineers                                # Managers who are not engineers. 'tom'
f = engineers > managers                                # Are all managers engineers? False
j = {'bob', 'sue'} < engineers                          # Are both engineers? true
k = (managers | engineers) > managers                   # All people is a superset of managers? True
n = managers ^ engineers                                # Who is only in one category? 'ann', 'bob', 'tom', 'vic'
m = (managers | engineers) - (managers ^ engineers)     # Intersection. 'sue'

# Filtering out duplications
withDuplicates = [1, 2, 2, 3, 3, 4, 4, 5]               # List with duplicates
noDuplicates = list(set(withDuplicates))                # [1, 2, 3, 4, 5]
