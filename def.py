def makerNested(n):
  def action(x):
    return x ** n
  return action
def makerLambda(n):
  return lambda x : x ** n
f = makerNested(2)
h = makerLambda(2)
f(3)                                              # 9
h(3)                                              # 9

# local scope with lambda
def func():
  x = 4
  action = (lambda n: x ** n)
  return action
x = func()
x(2)                                              # 16

# nonlocal variables
def tester(start):
  state = start
  def nested(label):
    nonlocal state
    print(label, state)
    state += 1
  return nested
a = tester(0)
a('spam')                                         # spam 0
a('ham')                                          # ham 1
a('eggs')                                         # eggs 2
