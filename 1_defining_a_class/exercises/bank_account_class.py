'''

    Class exercise

    Create a bank account class. It'll have a single attribute
    (per instance), transactions (it'll be a list of floats).
    Every time a deposit happens a positive float is added to the
    transactions.
    Every time a withdraw happens a negative float is added to the
    transactions.

        (a) Create two different accounts.
        (b) Add a number of transactions (positive/negative) to each account.
        (c) Show, for each account, number of transactions and the average
        amount per transaction, as well as the current balance. (assume it
        starts at 0).

'''


class Bank_account:
    def __init__(self, transactions):
        self.transactions = transactions

    def no_transactions(self):
        operations = self.transactions
        return len(operations)

    def av_amount(self):
        amount = sum(self.transactions)/len(self.transactions)
        return f"${round(amount, 2)}"

    def current_amount(self):
        amount = sum(self.transactions)
        return f"${round(amount, 2)}"


operations1 = [5.00, 10.50, 16, -2.50, -4.10, -1.30]
account1 = Bank_account(operations1)

operations2 = [-5.00, -10.50, -16, 2.50, 4.10, 1.30]
account2 = Bank_account(operations2)

print(
    f"""
    \n
    The number of transactions of the first account is
    {account1.no_transactions()}, the average amount per
    transaction is {account1.av_amount()} and the balance
    is {account1.current_amount()} .
    \n
    """
    )

print(
    f"""
    \n
    The number of transactions of the first account is
    {account2.no_transactions()}, the average amount per
    transaction is {account2.av_amount()} and the balance
    is {account2.current_amount()} .
    \n
    """
    )
