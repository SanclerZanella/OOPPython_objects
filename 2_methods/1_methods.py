'''

    Methods

    One of the core ideas of objects is to put data and functionality
    together, they're more tightly coupled that the object know what
    to do with the data received. By packaging the data and functionality
    together in a single object makes it easier to think about it, makes
    easier and maintain the code.

'''


class Foo:
    def __init__(self, x):
        self.x = x

    def x2(self):
        return self.x * 2


f = Foo(10)

vars(f)  # Output: {'x': 10}

f.x2()  # Invokes de method x2 on our f object. Output: 20

Foo.x2(f)  # The above line, f.x2(), is secretly rewritten to look like this!

# Examples


class Book:
    def __init__(self, title, author, price=30):
        self.title = title
        self.author = author
        self.price = price

    def nice_author_name(self):
        return ', '.join(reversed(self.author.split()))

    def price_with_tax(self):
        return self.price * 1.15


b1 = Book('Title1', 'John Smith')
b2 = Book('Title2', 'David Cohen')
b3 = Book('Title3', 'David Cohen', 25)

b1.price  # Output: 30, the default value for the price attribute
b2.price  # Output: 30, the default value for the price attribute
b3.price  # Output: 25, the reassingned value for the price attribute

b1.author  # Output: John Smith
b2.author  # Output: David Cohen

b1.nice_author_name()  # Output: Smith, John
b2.nice_author_name()  # Output: Cohen, David

b1.price_with_tax()  # Output: 34.5
b3.price_with_tax()  # Output: 28.75


# Has-a relationship -- composition
# Bookshelf class has-a Book class innit
class Bookshelf:
    def __init__(self):
        self.books = list()

    def add_books(self, *args):
        self.books += args

    def total_price(self):
        return sum([book.price for book in shelf.books])


shelf = Bookshelf()

shelf.add_books(b1, b2)  # Add b1 and b2 to the shelf
shelf.add_books(b3)  # Add b3 to the shelf

shelf.books  # Output: A list of objects

shelf.total_price()  # Output: sum of the price of all books in the shelf
