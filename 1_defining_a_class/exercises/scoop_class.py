'''

    Class exercise

    Create a class called scoop, where each instance is
    one scoop of ice cream with different flavors. Print
    the first flavor and then print all flavors in a loop.

'''


class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


flavor1 = Scoop('chocolate')
flavor2 = Scoop('vanilla')
flavor3 = Scoop('coffee')

print(flavor1.flavor)  # It'll print chocolate

flavors = [flavor1, flavor2, flavor3]

for fl in flavors:
    print(fl.flavor)
