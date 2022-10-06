'''
    Instead of write a method with the same name for every object
    to execute the same code, the python designers created functions
    that we could apply to each of these objects

    A simple way to find the methods of a object is using the help() function
    or dir()
'''

mylist = [10, 20, 30]
sum(mylist)  # sum() is a function, taking a list as an argument

# mylist.sum()  # This will not work

mylist.pop()  # pop() is a method, removes the final value from the list

# o.m()  # 'o' is the object and '.m(x)' is the method

len(mylist)  # len() is a function, return the iterable length

dir(mylist)  # Returns a list of methods of an object

help(list)  # Returns the doc string of this data type/object
