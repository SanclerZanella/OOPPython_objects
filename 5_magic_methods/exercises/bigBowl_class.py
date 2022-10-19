'''

    (1) Make it possible to run len() on our Bowl/BigBowl objects.  This
    will report the number of scoops in a bowl.

        b = Bowl()
        b.add_scoops(s1, s2, s3)
        len(b)  # return 3

    (2) Make it possible to "print" our Scoop and Bowl.  If I say

        print(s1)

        it'll print

        Scoop of chocolate

        mylist = [s1, s2, s3]

        print(mylist)

        [Scoop of chocolate, Scoop of vanilla, Scoop of coffee]

        print(b)

    Bowl with:
        1) Scoop of chocolate
        2) Scoop of vanilla
        2) Scoop of coffee

'''


class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f"Scoop of {self.flavor}"


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

    def __len__(self):
        return len(self.scoops)

    def __repr__(self):
        text = f"Bowl with:\n"
        # for i, flavor in enumerate(self.scoops, 1):
        #     text += f"\t{i}) Scoop of {flavor}\n"

        text += f"\n".join(f"\t{i}) Scoop of {flavor}"
                           for i, flavor in enumerate(self.scoops, 1))

        return text


class BigBowl(Bowl):
    max_scoops = 5


my_bowl = Bowl()
my_BigBowl = BigBowl()

my_bowl.add_scoop(scoop1, scoop2, scoop3, scoop4)
my_BigBowl.add_scoop(scoop1, scoop2, scoop3, scoop4, scoop5, scoop6)

print(len(my_BigBowl))
print(len(my_bowl))
print(scoop1)

list_of_scoops = [scoop1, scoop2, scoop3, scoop4, scoop5, scoop6]
print(list_of_scoops)
print(my_BigBowl)
