'''

    Classes (class) vs Functions (def)

    The structure of a class and the structure of a function are similar,
    but the behavior is different. When we create a function, two things
    happen, first we create a function object and second we define a new
    variable. The body of the function is not executed when we define the
    function, but when we execute the function.

'''


print('A')  # First output 'A' when we execute the code
class Person:
    print('B')  # Second output 'B' when the program defines the class
    def __init__(self, name):
        print('C')  # Fifth output 'C' when we create an object of type Person
        # calling the __init__ method(function) to build the new object

        self.name = name

    print('D')  # third output 'C' after 'B' when the program defines the class

    def greet(self):
        print('F')  # Last output 'F' when we run the method greet
        return f"Hello, {self.name}"

print('E')  # Fouth output 'E' after 'D' when the program finishes
# to define the class


p1 = Person('name1')  # Create new object of type Person
p2 = Person('name2')  # Create new object of type Person

print(p1.greet())  # Run method greet
print(p2.greet())  # Run method greet

print(dir(Person))  # Print all the methods in Person object
