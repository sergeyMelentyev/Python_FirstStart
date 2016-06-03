def makerNested(N):
  def action(X):
    return X ** N
  return action

f = makerNested(2)
f(3)                                              # 9

def makerLambda(N):
  return lambda X : X ** N

h = makerLambda(2)
h(3)                                              # 9

