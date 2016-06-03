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

def func():
  x = 4
  action = (lambda n: x ** n)
  return action

x = func()
x(2)                                              # 16

