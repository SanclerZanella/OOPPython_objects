# Any time we use an operator in python, it's being
# turned in a method call
2 + 2  # Output: 4
# Which is the same as:
int.__add__(2, 2)  # Output: 4
# Python is translating the plus(+) in a method call

str.__add__('abc', 'def')  # Output: 'abcdef'

name = 'Sancler'
'Hello, %s' % name  # Output: 'Hello, Sancler'
# In early python versions the % was the sign choosen to do
# string interpolations, python is translating % in a method
# Same can be executed like this:
'Hello, %s'.__mod__(name)  # Output: 'Hello, Sancler'


class Foo:
    def __init__(self, x):
        self.x = x


f = Foo('abcde')
f.x  # Output: 'abcde'
f[3]  # Output: Throw an error


class Foo:
    def __init__(self, x):
        self.x = x

    def __getitem__(self, index):
        return self.x[index]


f = Foo('abcde')
f[3]  # Output: 'd'
