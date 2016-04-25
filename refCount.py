import sys
print('My system is referencing object "1" for:', sys.getrefcount(1), 'times')

# Check for shared reference on objects
listFirst = [1, 2, 3]
listSecond = listFirst
print('Check for the same value:', listFirst == listSecond)                 # True
print('Check for the same object in ram:', listFirst is listSecond)         # True
listThird = [1, 2, 3]
print('Check for the same value:', listFirst == listThird)                  # True
print('Check for the same object in ram:', listFirst is listThird)          # False

# Check for shared reference on small numbers (cached)
x = 42
y = 42
print('Check for the same value:', x == y)                                  # True
print('Check for the same object in ram:', x is y)                          # True
