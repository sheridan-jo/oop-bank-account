"""
This program models a bank account. It contains a class called 'Account'
which contains the property 'transactions',as well as the methods
'get_balance()', 'deposit(amount)', and 'withdraw(amount)'.

Usage:
The 'transactions' property is a list of transaction instances.
The method 'get_balance(amount)' returns the account balance.
The method 'deposit(amount)' deposits money into the account.
The method 'withdraw(amount)' takes money out of the account.

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html

"""

class Account:
    """A class representing a bank account with a list of transactions"""

    def __init__(self):
        self.transactions = []  #  List of deposits and withdrawals
