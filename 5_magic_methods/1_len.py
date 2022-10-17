'''

    Len method

    len() looks for the __len__ inside the class, if it's not in there,
    then throw an TypeError, like:
        'TypeError: object of type 'Foo' has no len()'

    It has to return an integer.

'''


s = "abcd"
len(s)  # Output: 4, the number of characters in the string s

my_list = [10, 20, 30]
len(my_list)  # Count the number of elements in the list

d = {'a': 1, 'b': 2, 'c': 3}
len(d)  # Count the number of key-value pairs in the dictionary


class Foo:
    def __init__(self, x):
        self.x = x


f = Foo('abcd')
len(f)  # TypeError: object of type 'Foo' has no len()


# Magic method __whatever__
class Foo:
    def __init__(self, x):
        self.x = x

    def __len__(self):
        return len(self.x)


f = Foo('abcd')
len(f)  # Output: 4
f.__len__()  # Output: 4, not recommended way, but works
