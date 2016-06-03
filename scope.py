var = 99                            # global var

def local():                        # change local var
  var = 0

def globalOne():                    # chage global var
  global var
  var += 1

def globalTwo():                    # chage global var
  import scope
  scope.var += 1

def globalThree():                  # chage global var
  import sys
  glob = sys.modules['scope']
  global.var += 1
