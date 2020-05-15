
'''
def c2f(n):
    return "Avengers"
'''

def func(mode):

    def c2f():
        return "Avengers"

    def f2c():
        return "Star Wars"

    if (mode == 0):
        return c2f   # Returning a function object
    else:
        return f2c

# --------------------------------

x = func(1)
print(x())
