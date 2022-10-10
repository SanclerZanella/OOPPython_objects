'''

    Use our existing Person and BankAccount classes.  Make it possible
    for a person to have one or more bank accounts.  So we can say:

    p1.add_account(ba1)
    p1.add_account(ba2)

    p1.all_balances()           # returns a list of floats representing
                                  balances
    p1.current_total_balance()  # gives the total balance across all accounts

    p1.average_transaction_amount()  # returns the average amount of
                                       transactions across all accounts


'''


class Person:
    def __init__(self, name, email, phNumber):
        self.name = name
        self.email = email
        self.phNumber = phNumber
        self.bankAccounts = list()

    def add_account(self, *args):
        self.bankAccounts += args

    def all_balances(self):
        return [account.current_balance() for account in self.bankAccounts]

    def current_total_balance(self):
        return sum(
            [account.current_balance() for account in self.bankAccounts]
            )

    def average_transaction_amount(self):
        transactions = list()
        for account in self.bankAccounts:
            transactions.extend(account.transactions)

        return round(sum(transactions)/len(transactions), 2)


class Bank_account:
    def __init__(self, transactions):
        self.transactions = transactions

    def no_transactions(self):
        operations = self.transactions
        return len(operations)

    def av_amount(self):
        amount = sum(self.transactions)/len(self.transactions)
        return f"${round(amount, 2)}"

    def current_balance(self):
        amount = sum(self.transactions)
        return round(amount, 2)


operations1 = [5.00, 10.50, 16, -2.50, -4.10, -1.30]
account1 = Bank_account(operations1)

operations2 = [-2.50, -5.25, -8, 1.25, 2.05, 0.65]
account2 = Bank_account(operations2)

person1 = Person('Sancler', 'sancler@email.com', '0101-0101')

person1.add_account(account1, account2)

print(person1.all_balances())
print(person1.current_total_balance())
print(person1.average_transaction_amount())
