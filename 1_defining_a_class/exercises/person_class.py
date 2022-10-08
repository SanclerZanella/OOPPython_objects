'''

    Class exercise

    Create class called person, with name, email and phone
    number. Then create several people, and iterate over them in a list
    and print their names, change the email address of one person and show
    that it has changed by printing the list a second time

'''


class Person:
    def __init__(self, name, email, phNumber):
        self.name = name
        self.email = email
        self.phNumber = phNumber


person1 = Person('Sancler', 'sancler@email.com', '0101-0101')
person2 = Person('Anamim', 'anamim@email.com', '0202-0202')
person3 = Person('John', 'john@email.com', '0303-0303')

people = [person1, person2, person3]

for person in people:
    print(f"{person.name} phone is {person.phNumber}, email is {person.email}")

person1.email = 'sanclerzanella@email.com'

for person in people:
    print(f"{person.name} phone is {person.phNumber}, email is {person.email}")
