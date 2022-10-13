'''

    Basic inheritance

    Inheritance is extends a first class that already works, taking advantage
    of everything in the first class adding it to the new class with new
    attributes and methods in the new class.

    How does it happens when we call a method?
        a.b
        (1) does 'b' exist as an attribute on 'a'?
        (2) does 'b' exist as an attribute on 'a' class?
        (3) does 'b' exist as an attribute on 'a' parent class?
        repeat this until we get to a class whose parent is "object"
        (4) does 'b' exist as an attribute on object?

    The point with inheritance is don't repeat myself, don't repeat data.

'''


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"


p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())


# The Employee inherit from the class Person
class Employee(Person):
    def __init__(self, name, id):
        super().__init__(name)  # super() gives back on which I can run it
        self.id = id


e1 = Employee('employee1', 1)
e2 = Employee('employee2', 2)

print(e1.greet())
print(e2.greet())
