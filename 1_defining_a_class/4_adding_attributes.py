'''
    Adding attributes
'''


class Foo(object):
    pass


f = Foo()

vars()  # Without argument, returns a dictionary of the global variables.


def bar():
    vars()  # returns a dictionary of the local variables of this function.


vars(f)  # It'll return a dictionary of the attributes added to 'f'
# not inherited

print(vars(f))

f.x = 100
f.y = [10, 20, 30]

dir(f)  # It'll return all the methods of 'f' the default methods
# the added methods (x and y)

vars(f)  # It'll return a dictionary of the added methods (x and y)
# to 'f', where the key will be the method name and the value the
# method value like {'x': 100, 'y': [10, 20, 30]}

g = Foo()  # Second object of type 'Foo'

# Here we have two different objects of the same type 'Foo',
# They behave in the same way in general, they have the same
# methods availabe to them, but the actual values are different
# Changing one is not changing another

g.a = {'a': 1, 'b': 2, 'c': 3}
g.b = {10, 20, 30, 40, 50}

# If you check the methods added to each object of type 'Foo', they will
# return different objects, because each object is different
vars(g)
vars(f)

# Add attributes to a already created class is not a consistent way to work
# with objects.
