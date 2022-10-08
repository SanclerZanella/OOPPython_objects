'''

    To give more flexiblity to the class when creating different new objects
    we can add parameters to the __init__ method.
    These parameters added to the '__init__' method are now required when
    creating a new object/instance of the class, is necessary to pay attention
    to how many arguments are necessary when invoking a class.
    But default values can be provided, in this case the class can be invoked
    without arguments.

'''


class Foo(object):
    def __init__(self, x, y):
        '''
            'x' and 'y' are local variables assigned as value of the
            object attributes (self.x and self.y).
        '''
        self.x = x
        self.y = y


f = Foo(10, 20)  # Foo is called with two arguments (10 and 20), these
# two values were added after 'self' when the class was created and now
# two arguments are required when invoking Foo ('x' and 'y')
# because self is automatically called by python

vars(f)  # output: {'x': 10, 'y': 20}


class Foo(object):
    def __init__(self, x=888, y=999):
        '''
            in this case 'x' and 'y' are parameters with default values
            but they can be reassigned when invoking the class.
        '''
        self.x = x
        self.y = y


class Foo(object):
    def __init__(self, x, *args):
        '''
            in this case 'x' doesn't have a default value and it's using
            *args as parameter.
        '''
        self.x = x
        self.y = args
