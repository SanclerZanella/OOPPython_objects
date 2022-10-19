'''

    (3) Make len() and print() work on the Shopping Cart.  If I say
        len(sc), it'll return the number of items in the cart.

        print(sc)

        It'll show each item in the cart -- name, per-unit price,
        quantity, and total price for that item.  *PLUS* it'll show the
        total price of all items

        item1    2    $1    $2
        item2    6    $3    $18
        -----------------------
        Total               $20

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

    def __len__(self):
        return sum([qty for price, qty in self.products.values()])

    def __repr__(self):
        text = ""
        products = self.products

        for item_info in products.keys():
            prod_value = products.get(item_info)
            qty = prod_value[0]
            price = prod_value[1]
            subtotal = qty * price

            text += f"{item_info:10} {qty:3} ${price:3} ${subtotal:3}\n"

        text += f"---------------------------\nTotal\t${self.total()}"

        return text


class OnlineShoppingCart(ShoppingCart):
    def total(self):
        normal_total = super().total()
        return (normal_total * 1.05) + 10


osc = OnlineShoppingCart()

osc.add('Book', 30, 3)
osc.add('Medicine', 50, 1)
# print(osc.total())

print(len(osc))
print(osc)
