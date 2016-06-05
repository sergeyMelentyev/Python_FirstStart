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
