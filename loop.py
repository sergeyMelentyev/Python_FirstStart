A = Y if X else Z                             # ternary expression
A = [Y, Z][bool(X)]                           # bool function with offset
A = X or Y or None                            # assings first nonempty object or None

A = [(1, 2), (3, 4), (5, 6)]
for (a, b) in A:
  print(a, b)

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:      # tuple in the loop
  print(a, b, c)

L = [1, 2, 3, 4, 5]                           # add one to each item in list via for loop
for i in range(len(L)):
  L[i] += 1

i = 0                                         # add one to each item in a list via while loop
while i < len(L):
  L[i] += 1
  i += 1

