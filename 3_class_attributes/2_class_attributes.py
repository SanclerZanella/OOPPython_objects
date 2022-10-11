'''

    Class Attributes

    class attribute is different from instance attribute.

    Class attribute could be used at least in two different ways:
        (1) When we have a value that gonna be using throughout a class
            and don't wanna hard code that value, then the class
            attribute is useful, because we can just refer to it all
            the time there.
        (2) When we have a resource that is shared among different
            instances and we don't want this resource outside the
            class as a global variable.

    If we ask for a.b:
        (1) Python looks for "b" attribute on "a" (The instance)
        (2) If not, then look for "b" on type(a) (The class)
        (3) If not, then look for "b" on parent object, if this is the case
        (4) If not, then Python throw an error.

'''


class Person:
    # class attribute
    population = 0  # This defines Person.population = 0

    def __init__(self, name):
        Person.population += 1
        self.name = name


print(f"Before, population = {Person.population}")
p1 = Person('name1')
p2 = Person('name2')
print(f"After, population = {Person.population}")
print(f"After, population = {p1.population}")
print(f"After, population = {p2.population}")
