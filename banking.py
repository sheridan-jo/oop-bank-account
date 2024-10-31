"""
Python Development II
Assignment 5 - OOP Bank Account
John O.
October 31, 2024

This program models a bank account. It contains a class called 'Account'
which contains the property 'transactions',as well as the methods
'get_balance()', 'deposit(amount)', and 'withdraw(amount)'.

Usage:
    - The 'transactions' property is a list of transaction instances.
    - The method 'get_balance(amount)' returns the account balance.
    - The method 'deposit(amount)' deposits money into the account.
    - The method 'withdraw(amount)' takes money out of the account.

Imports:
    Decimal: Used for accurate representation of dollar values.
    datetime: Provides date and time for transaction timestamps.

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html



"""

from decimal import Decimal
import datetime

class Account:
    """
    A class representing a bank account with a list of transactions

    Attributes:
        transactions: A list of deposits and withdrawals
    """

    def __init__(self):
        self.transactions = []  # Initializes an empty transaction list for each account.

class Transaction:
    """
    A class representing a deposit or withdrawal from an account.

    Attributes:
        amount (Decimal): The amount of the transaction.

        timestamp (datetime): The date and time when the transaction occurred.
            Set to current date and time if no timestamp is provided.
    """

    def __init__(self, amount, timestamp=None):
        self.amount = Decimal(amount)  #  Converts 'amount' to Decimal

        #  Sets timestamp to current date and time if no argument is entered
        self.timestamp = timestamp or datetime.datetime.now()

