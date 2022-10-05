'''
Everything is an object in python and it means:
    (1) Everything has a type/class:
        In python system each kind of data works in  a certain predictable
        kind of way like strings, integers, lists, dictionaries,...
        This predictable behaviour gives consistency to build our code.

        A type is like a factory, a creator o new objects.
        The object itself is what is created.
        Like an ice cream machine making ice cream, a print making newspapers,
        so we can distinguish between the maker and makee as it were.
        The factory's factory is type, every class's type is "type".

        In python classes are also objects, you can pass them arround as
        argument of functions for example. The type of every class is type.

    (2) Everything has an attribute:
        Every object in python has attributes and everything is an object.
        To access an attribute or method is necessary to use "." after the name
        like:
                                a = 'abcd'
                                a.upper()

        Every type is an object and every object has attributes

'''

# start______________ (1) Everything has a type/class ________________________

# x is the variable and 100 is the object.
x = 100
type(x)  # It will output the data type "int"

x = "abcd"
type(x)  # It will output the data type "str"

x = [10, 20, 30]
type(x)  # It will output the data type "list"

int("123")  # int() is a class which create an integer from a string.
str(123)  # str() is a class which create an string from an integer.
list("abcd")  # list() is a class which create a list from an iterable.

# The type of every class is "type"
type(int)  # It will output the data type "type"
type(str)  # It will output the data type "type"
type(list)  # It will output the data type "type"

# Also, The type of type is "type", because it's a class
# and everything in python is an object
type(type)  # It will output the data type "type"

# end______________ (1) Everything has a type/class ________________________


# start______________ (2) Everything has an attribute ________________________

# a   identifier = name = variable or function... an object of some sort
# How it'll be search is LEGB (Local Enclosing Global Built-in)
# LEGB is an abbreviation for (Local Enclosing Global Built-in) followed
# by the Python interpreter when executing a code. The LEGB rule in Python
# is a name searching algorithm where Python looks up scopes
# in a particular order.

# a.b   ".b" means: Look for the name ("attribute") "b"
# inside of the object "a"

a = 'abcd'
dir(a)  # It'll output all the methods of "a"

# Use the methods name .upper()
a.upper()  # It'll output all the attributes of "ABCD"

import os

# Ask for an attribute of os
os.sep  # Describes what character or string separates elements
# in the path

os.sep = "hahahaha"  # It'll output "hahahaha"

os.opp_course = "Python Objects"  # Add new attribute to this object
os.opp_course  # It'll output "Python Objects"
