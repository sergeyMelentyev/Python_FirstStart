# Basic function call
def echo(message):
    print(message)

echo('Direct function call')
x = echo
x('Indirect function call')


def indirect(function, argument):
    function(argument)

indirect(echo, 'Argument call')


schedule = [(echo, 'Embedded call'), (echo, 'Embedded call')]
for (func, arg) in schedule:
    func(arg)


# Nested function call
def maker_nested(n_arg):
    def action(x_arg):
        return x_arg ** n_arg
    return action


def maker_lambda(m_arg):
    return lambda y_arg: y_arg ** m_arg

f = maker_nested(2)
h = maker_lambda(2)
f(3)                                                                        # 9
h(3)                                                                        # 9


# local scope with lambda
def func():
    local_var = 4
    action = (lambda n_arg: local_var ** n_arg)
    return action

anyName = func()
anyName(2)                                                                  # 16


# nonlocal variables
def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

new_name = tester(0)
new_name('spam')                                                            # spam 0
new_name('ham')                                                             # ham 1
new_name('eggs')                                                            # eggs 2


# Function attributes
def func_name(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested

b_name = func_name(0)
b_name('spam')                                                              # spam 0
b_name('eggs')                                                              # eggs 1


# Function arguments
def changer(a_arg, b_arg):
    a_arg = 2                                                               # passed by value
    b_arg[0] = 'spam'                                                       # passed by pointer

one = 1
two = [1, 2]
changer(one, two)
print(one, two)                                                             # 1, ['spam', 2]


def f(a, b, c):
    print(a, b, c)

f(1, 2, 3)                                                      # matches from left to right
f(c=3, a=1, b=2)                                                            # matches by name


def g(a, b=2, c=3):                                                         # default values
    print(a, b, c)


# Function collection arguments
def tuple_func(*args):
    print(args)

tuple_func()                                                                # ()
tuple_func(1)                                                               # (1,)
tuple_func(1, 2, 3)                                                         # (1, 2, 3)


def dict_func(**args):
    print(args)

dict_func()                                                                 # {}
dict_func(a=1, b=2)                                                         # {'a': 1, 'b': 2}
