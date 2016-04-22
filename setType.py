# No sequences no key no mapping object
x = set('spam')                                             # {'s', 'p', 'a', 'm'}
y = {'s', 'p', 'a', 'm', 'm', 'n'}                          # {'s', 'p', 'a', 'm', 'm', 'n'}

# Check for intersection
intersection = x & y                                        # {'p', 's', 'm', 'a'}

# Check for union
union = x | y                                               # {'n', 's', 'm', 'p', 'a'}

# Check for difference
diff = y - x                                                # {'n'}

# Check for superset
superSet = x > y                                            # False

# Filtering out duplications
duplication0 = list({1, 2, 2, 3, 3, 4, 5})                  # set literal
duplication1 = list(set([1, 2, 2, 3, 3, 4, 5]))             # function call

# Finding differences
differ = set(y) - set(x)                                    # {'n'}

