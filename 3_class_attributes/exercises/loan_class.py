'''

    Create a Loan class. Each time someone creates a new Loan, it's
    for a certain amount of money.  That money is taken from the
    bank's available assets.

    l1 = Loan(500)
    l2 = Loan(200)
    l3 = Loan(700)  # raises an exception -- ValueError to indicate no money
    l1.repay(500)
    l3 = Loan(700)  # now it'll work, because the bank has sufficient funds

'''


class Loan:
    amount = 1000

    def __init__(self, value):
        if value <= Loan.amount:
            self.value = value
            Loan.amount -= value
        else:
            raise ValueError("Bank doesn't have enough")

    def repay(self, value):
        self.value -= value
        Loan.amount += value


l1 = Loan(500)
l2 = Loan(200)
# l3 = Loan(700)
l1.repay(500)
l3 = Loan(700)
