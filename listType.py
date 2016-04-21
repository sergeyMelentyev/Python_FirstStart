# Multidimensional array
listArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# first row is [1, 2, 3]
# first column in each row is 1 and 4 and 7
print(listArray[1])                 # [4,5,6]
print(listArray[1][2])              # 6

# Get item from each second column
listNewArray = [row[1] for row in listArray]
print(listNewArray)                 # [2,5,8]

# Get item from each second row with filter
filteredArray = [row[1] for row in listArray if row[1] % 2 == 0]
print(filteredArray)                # [2,8]

# Get diagonal item from matrix
diaArray = [listArray[i][i] for i in [0, 1, 2]]
print(diaArray)                     # [1,5,9]
