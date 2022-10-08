'''

    In order to create a new class or data type we must use the 'class'
    special keyword and after the 'class' keyword give a name to the class
    starting by capital letter by standards like 'Foo'.

    Old-style classes do not inherit from object. Old-style instances are
    always implemented with a built-in instance type.
    New-style classes in Python 3 implicitly inherit from object, so there
    is no need to specify MyClass(object) anymore.

'''


class Foo(object):
    '''
        This is an one line class just to introduce the class syntax
        it inherits from object and there is no body.
    '''
    pass


# A new type of data was created the 'Foo' type.

type(Foo)  # The type of the class Foo is 'type', because the type of every
# class in python is 'type'

# and to use this class/data type I have to create an
# object/instance of that class

f = Foo()

type(f)  # It'll return __main__.Foo, because it's the default name space

# Every single object in python is not only a type but also has attributes
dir(Foo)  # It'll return a list of the Foo attributes, in this case it will
# return the default attributes (inherited from another class)

dir(f)  # Same output as dir(Foo)

f.new_method = "Hello World!"
dir(f)  # It'll return the default methods
# plus the new created method 'new_method'
