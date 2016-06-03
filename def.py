def makerNested(N):
  def action(X):
    return X ** N
  return action

def makerLambda(N):
  return lambda X : X ** N

f = makerNested(2)
h = makerLambda(2)
f(3)                                              # 9
h(3)                                              # 9
