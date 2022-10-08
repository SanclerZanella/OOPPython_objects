'''

    Consistently creating methods for a class

    Basicly an object is created in two stages, you first create
    with a method called '__new__', this method is called automaticly
    when we create a new object, after '__new__' is finished of create
    a new object of the new type (in this case 'Foo') it looks for the
    '__init__' method, if it exists it adds the attributes to the new object.

    '__init__' gets a single argument called 'self' like '__init__(self)' it's
    like the keyword 'this' in other languages, 'self' gets the current object
    to do whatever has to do. 'self' is just a convention, in theory you can
    call your first parameter whatever you want, but everyone in the python
    world use the name 'self'.

    'self' is actually the object itself, is the current instance
    of foo itself, it's always the first parameter in every single method
    in the class.

    '__init__' add the methods to the object that 'self' points to.
    It doesn't return a value, because the most important is the attributes
    or changes it adds to the object.

    The class is invoked with parentheses (a new object/instance of the class
    is created), that invokes '__new__' that creates the new object, '__new__'
    looks for '__init__' and invokes it to add new attributes to new objects,
    and then '__new__' return the new object with the new attributes added.

    Any new attribute can be added outside the class but this not consistent
    and this is not recomended.

    Attributes should be created only in the class, but you can assing values
    to these attributes outside the class.

'''


from ast import For


class Foo(object):
    def __init__(self):
        '''
            __init__ is the method that is invoked automatically
            when a new a new Python object is created
        '''
        self.x = 100
        self.y = [10, 20, 30]


f = Foo()  # The class is invoked with parentheses
vars(For)  # It'll output a dictionary of the 'f' attributes
# without the default attributes, in this case it'll be
# {'x': 100, 'y': [10, 20, 30]}

g = Foo()
vars(g)  # It'll output the same as vars(f), because the behavior is
# now consistent

f.x  # It'll output 100

f.x = 200
vars(f)  # It'll output {'x': 200, 'y': [10, 20, 30]}

f.y.append(40)  # It'll append to the value of 'y', which is a list
vars(f)  # It'll output {'x': 200, 'y': [10, 20, 30, 40]}
