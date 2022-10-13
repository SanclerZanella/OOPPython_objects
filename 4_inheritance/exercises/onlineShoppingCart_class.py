'''

    Take our existing ShoppingCart class.  Create a subclass called
    OnlineShoppingCart.  In this case, the "total" method will add
    another $10 + 5% of the total for shipping costs.

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


class OnlineShoppingCart(ShoppingCart):
    def total(self):
        normal_total = super().total()
        return (normal_total * 1.05) + 10


osc = OnlineShoppingCart()

osc.add('Book', 30, 1)
print(osc.total())
