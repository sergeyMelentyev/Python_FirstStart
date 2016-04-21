# Multidimensional array
listArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# first row is [1, 2, 3]
# first column in each row is 1 and 4 and 7

# Get item from each second column
listNewArray = [row[1] for row in listArray]                        # [2, 5, 8]

# Get item from each second row with filter
filteredArray = [row[1] for row in listArray if row[1] % 2 == 0]    # [2, 8]

# Get diagonal item from matrix
diaArray = [listArray[i][i] for i in [0, 1, 2]]                     # [1, 5, 9]

# Create a list with range
rangeList0 = list(range(4))                                         # [0, 1, 2, 3]
rangeList1 = list(range(-6, 7, 2))                                  # [-6, -4, -2, 0, 2, 4, 6]
rangeList2 = [[x ** 2, x ** 3] for x in range(3)]                   # [[0, 0], [1, 1], [4, 8]]

# Calculate sum in each row
sumRow0 = list(map(sum, listArray))                                 # [6, 15, 24]

# Create a key/value table of row sums
sumRow1 = {i: sum(listArray[i]) for i in range(3)}                  # {0: 6, 1: 15, 2:24}
