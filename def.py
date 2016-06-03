# Basic function call
def echo(message):
  print(message)
echo('Direct function call')
x = echo
x('Indirect function call')

def indirect(func, arg):
  func(arg)
indirect(echo, 'Argument Call')

schedule = [(echo, 'Embedded call'), (echo, 'Embedded call')]
for (func, arg) in schedule:
  func(arg)

# Nested function call
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

# function attributes
def funcName(start):
  def nested(lable):
    print(label, nested.state)
    nested.state += 1
  nested.state = start
  return nested
b = fyncName(0)
b('spam')                                         # spam 0
b('eggs')                                         # eggs 1

# function arguments
def changer(a, b):
  a = 2                                           # changes local name, passed by value
  b[0] = 'spam'                                   # changes shared object in place, passed by pointer
one = 1
two = [1, 2]
changer(one, two)
print(one, two)                                   # 1, ['spam', 2]

def f(a, b, c):
  print(a, b, c)
f(1, 2, 3)                                        # matches from left to right
f(c=3, a=1, b=2)                                  # matches by name

def g(a, b=2, c=3):                               # default values
  print(a, b, c)

# function collection arguments
def tuplFunc(*args):
  print(args)
tupleFunc()                                       # ()
tupleFunc(1)                                      # (1,)
tupleFunc(1, 2, 3)                                # (1, 2, 3)

def dictFunc(**args):
  print(args)
dictFunc()                                        # {}
dictFunc(a=1, b=2)                                # {'a': 1, 'b': 2}
