'''

    Create a ShoppingCart class.

    sc = ShoppingCart()
    sc.add('book', 30, 1)    # name, price-per-unit, quantity
    sc.add('toothbrush', 3, 4)

    sc.remove('toothbrush')   # removes one toothbrush -- or removes
                              # the item altogether if the quantity is 0

    sc.total()  # returns the total price of items in the shopping cart

'''


class Bag:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.quantity = qty

    def total_bag(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"({self.name}, {self.price}, {self.quantity})"


class ShoppingCart:
    def __init__(self):
        self.products = list()

    def add(self, *args):
        self.products += args

    def remove(self, product):
        for bag in self.products:
            if product.lower() == bag.name:
                if bag.quantity != 0:
                    bag.quantity -= 1
                else:
                    self.products.remove(bag)

    def total(self):
        total_in_cart = 0
        for bag in self.products:
            total_in_cart += bag.total_bag()

        return total_in_cart


b1 = Bag('book', 30, 1)
b2 = Bag('toothbrush', 3, 4)


sc = ShoppingCart()
sc.add(b1, b2)
print(sc.products)

sc.remove('Toothbrush')

print(sc.products)
print(sc.total())
