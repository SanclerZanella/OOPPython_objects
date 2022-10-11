'''

    Modify the Bowl class, such that adding a new scoop to the bowl
    will only work if you have fewer than 3 scoops.  In other words: max 3
    scoops per bowl.

    Adding a new scoop to a bowl that is already full will be silently
    ignored.


'''


class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


scoop1 = Scoop('chocolate')
scoop2 = Scoop('vanilla')
scoop3 = Scoop('coffee')
scoop4 = Scoop('Honey')


class Bowl:
    max_scoops = 3  # class attribute

    def __init__(self):
        self.scoops = list()

    def add_scoop(self, *args):
        self.scoops += args[:Bowl.max_scoops - len(self.scoops)]
        # for scoop in args:

        #     if len(self.scoops) == Bowl.max_scoops:
        #         break

        #     self.scoops.append(scoop)

    def flavors(self):
        return ', '.join(scoop.flavor for scoop in self.scoops)


my_bowl = Bowl()

my_bowl.add_scoop(scoop1, scoop2, scoop4, scoop3)

print(my_bowl.flavors())
