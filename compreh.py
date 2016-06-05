# Simple iteration
res = []
for x in 'spam':                                                # For loop
    res.append(ord(x))
print(res)

res = list(map(ord, 'spam'))                                    # Function call
print(res)

res = [ord(x) for x in 'spam']                                  # List comprehensions
print(res)


# Simple iteration with arbitrary expression
res = list(map((lambda x_arg: x_arg ** 2), range(10)))          # Function call
print(res)

res = [x_arg ** 2 for x_arg in range(10)]                       # List comprehensions
print(res)


# Simple iteration with nested loop
res = []
for x in range(5):                                              # For loop
    if x % 2 == 0:
        res.append(x)
print(res)

res = list(filter((lambda x_arg: x_arg % 2 == 0), range(5)))    # Function call
print(res)

res = [x_arg for x_arg in range(5) if x_arg % 2 == 0]           # List comprehensions
print(res)


# Nested clauses
res = []
for x in [0, 1, 2]:                                             # For loop
    for y in [10, 20, 30]:
        res.append(x + y)
print(res)

res = [x + y for x in [0, 1, 2] for y in [10, 20, 30]]          # List comprehensions
print(res)

res = []
for x in range(5):                                              # For loop
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append((x, y))
print(res)

res = [(x, y) for x in range(5) if x % 2 == 0                   # List comprehensions
       for y in range(5) if y % 2 == 1]
print(res)


# Multidimensional array
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]

res = [M[i][i] for i in range(len(M))]                          # Diagonals
print(res)

res = [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
print(res)


# Changing matrix
res = []
for row in M:                                                   # For loop
    tmp = []
    for col in row:
        tmp.append(col + 10)
    res.append(tmp)
print(res)

res = [[col + 10 for col in row] for row in M]                  # List comprehensions
print(res)
