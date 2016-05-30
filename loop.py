A = Y if X else Z                         # ternary expression
A = [Y, Z][bool(X)]                       # bool function with offset
A = X or Y or None                        # assings first nonempty object or None

A = [(1, 2), (3, 4), (5, 6)]
for (a, b) in A:
  print(a, b)

