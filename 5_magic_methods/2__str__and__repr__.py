'''

__str__ and __repr__ methods

__str__ is a method inherited from object that transform the class in a string.
__str__ is the string version of an object, for common usage, for end users.

__repr__ is the string version of an object, for developers.
The __repr__ should be a string that we can evaluate, __repr__ can be used in
place of __str__ but not __str in place of __repr__, if __str__ is not in the
object.

'''


class Foo:
    def __init__(self, x):
        self.x = x

    def __len__(self):
        return len(self.x)


f = Foo('abcd')

# print(f)  # Output: <__main__.Foo object at 0x0000023A8CABA7F0>


class Foo:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"I'm a Foo, with vars = {vars(self)}"


f = Foo('abcd')

# print(f)  # Output what the __str__ method is returning in the class Foo
# str(f) -> f.__str__()


class Foo:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"[str] I'm a Foo, with vars = {vars(self)}"

    def __repr__(self):
        return f"[repr] I'm a Foo, with vars = {vars(self)}"


f = Foo('abcd')

# print(f)  # Output: [str] I'm a Foo, with vars = {'x': 'abcd'}

# my_list = [f]
# print(my_list)  # Output: [[repr] I'm a Foo, with vars = {'x': 'abcd'}]


class Foo:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f"[repr] I'm a Foo, with vars = {vars(self)}"


f = Foo('abcd')

print(f)  # Output: [[repr] I'm a Foo, with vars = {'x': 'abcd'}]
# python will print __repr__ in place of __str__ if __str__ is not
# in thr object
