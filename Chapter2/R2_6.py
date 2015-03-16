'''
R-2.6: If the parameter to the make_payment method of the CreditCard class were
negative number, that would have the effect of raising the balance on the account.
Revise the implementation so that it raises a ValueError if a negative value is
sent.
'''

# Original Code:


def make_payment(self, amount):
    self._balance -= amount

# We can modify to include ValueError as follows:


def make_payment(self, amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    self._balance -= amount
