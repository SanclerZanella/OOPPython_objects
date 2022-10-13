'''

    Take our existing Bowl class (for ice cream), and create a
    subclass called BigBowl.  A BigBowl is just like a Bowl, except
    that it has a maximum of 5 scoops, not 3.

'''


class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


scoop1 = Scoop('chocolate')
scoop2 = Scoop('vanilla')
scoop3 = Scoop('coffee')
scoop4 = Scoop('Honey')
scoop5 = Scoop('Nutella')
scoop6 = Scoop('Strawberry')


class Bowl:
    max_scoops = 3

    def __init__(self):
        self.scoops = list()

    def add_scoop(self, *args):
        self.scoops += args[:self.max_scoops - len(self.scoops)]

    def flavors(self):
        return ', '.join(scoop.flavor for scoop in self.scoops)


class BigBowl(Bowl):
    max_scoops = 5


my_BigBowl = BigBowl()

my_BigBowl.add_scoop(scoop1, scoop2, scoop3, scoop4, scoop5, scoop6)

print(my_BigBowl.flavors())
