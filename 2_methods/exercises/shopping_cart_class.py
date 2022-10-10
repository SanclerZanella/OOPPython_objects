'''

    Create a ShoppingCart class.

    sc = ShoppingCart()
    sc.add('book', 30, 1)    # name, price-per-unit, quantity
    sc.add('toothbrush', 3, 4)

    sc.remove('toothbrush')   # removes one toothbrush -- or removes
                              # the item altogether if the quantity is 0

    sc.total()  # returns the total price of items in the shopping cart

'''


class ShoppingCart:
    def __init__(self):
        self.products = dict()

    def add(self, product, price, quantity):
        if product in self.products:
            previous_quantity = self.products[product][1]
            self.products[product] = (price, previous_quantity + quantity)
        else:
            self.products[product] = (price, quantity)

    def remove(self, product):
        if product in self.products:
            price, quantity = self.products[product]
            if quantity == 1:
                del(self.products[product])
            else:
                self.products[product] = (price, quantity - 1)

    def total(self):

        return sum([price * quantity
                    for price, quantity in self.products.values()])


sc = ShoppingCart()
sc.add('Book', 30, 1)
sc.add('toothbrush', 4, 4)

sc.remove('toothbrush')

print(sc.total())
