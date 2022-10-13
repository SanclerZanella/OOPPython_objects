'''

    Take our existing Person class, and add a subclass, called
    VerbosePerson.  This class works the same way as Person, except that
    the "greet" method doesn't just return "Hello, NAME" but rather
    something longer than that.

'''


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"


class VerbosePerson(Person):
    # def greet(self):
    #     return f"{super().greet()}! What's the craic?!"
    def greet(self):
        return f"Hello {self.name}! What's the craic?!"

    def goodbye(self):
        return f"{self.name} see you later!"


vp = VerbosePerson('John')

print(vp.greet())
print(vp.goodbye())
