'''

    The whole point of data structures is that we can organize our data
    in ways that makes sense to us but also makes sense for the computer,
    in a way that it's efficient for the computer to store, efficent to us
    to retrieve or search through.

    Even though put our data in a list of dictionaries is totally reasonable
    and normal in python it's not the high level of abstraction.
    Think in a high level of abstraction in programming allows us to think in
    better solutions, more organized code and maintain more complex programs.

'''


# Think in a low level of abstraction, we created
# a list of objects holding data about computers in a place
computers = [
    {
        'brand': 'Apple',
        'year': 2014,
    },
    {
        'brand': 'HP',
        'year': 2016,
    },
    {
        'brand': 'Lenovo',
        'year': 2016,
    },
    {
        'brand': 'Apple',
        'year': 2010,
    },
]

# It'll print each computer brand and year in the 'computers' list
for one_computer in computers:
    print(f"{one_computer['brand']} from {one_computer['year']}")

# To print just those from 2016 we can add an if statement in the loop
for one_computer in computers:
    if(one_computer['year'] == 2016):
        print(f"{one_computer['brand']} from {one_computer['year']}")


# Think in a high level of abstraction, we created a new data type
# to hold the computers data, knowing that each computer has consistent
# attributes like 'brand' and 'year', we created a class
# to hold the computers data.
class Computer:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


# Created a new objects/instances of 'Computer', for each computer in the place
c1 = Computer('Apple', 2014)
c2 = Computer('HP', 2016)
c3 = Computer('Lenovo', 2016)
c4 = Computer('Apple', 2010)

# list of objects
my_computers = [c1, c2, c3]

# It'll print each computer brand and year in the 'my_computers' list
# Accessing each object item methods
for one_computer in my_computers:
    print(f"{one_computer.brand} from {one_computer.year}")

# To print just those from 2016 we can add an if statement in the loop
for one_computer in my_computers:
    if(one_computer.year == 2016):
        print(f"{one_computer.brand} from {one_computer.year}")

# Using the class we'll get the same result as using the list of dictionaries
# but using the class 'Computer' the code was semantically improved
# and as well become easier to scalate the code adding new fields (attributes)
# to the class, it give us a higher level way of thinking about our data.


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


all_books = list()
while True:
    title = input("Enter the title (or <enter> to stop): ").strip()

    if not title:
        break

    author = input("Enter the author: ").strip()
    price = float(input("Enter the price: ").strip())

    all_books.append(Book(title, author, price))

print(all_books)
