'''

    Create a Bowl class.  We can put scoops in the bowl!

    b = Bowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3)
    b.flavors()  # returns a string of "chocolate, vanilla, coffee"

'''


class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


scoop1 = Scoop('chocolate')
scoop2 = Scoop('vanilla')
scoop3 = Scoop('coffee')


class Bowl:
    def __init__(self):
        self.scoops = list()

    def add_scoop(self, *args):
        self.scoops += args

    def flavors(self):
        return ', '.join(scoop.flavor for scoop in self.scoops)


my_bowl = Bowl()

my_bowl.add_scoop(scoop1, scoop2, scoop3)

print(my_bowl.flavors())
