"""
Python Development II
Assignment 5 - OOP Bank Account
John O.
November 10, 2024

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

#  Code for the Account class

class Account:
    """
    A class representing a bank account with a list of transactions

    Attributes:
        transactions: A list of deposits and withdrawals
    """

    #  Account class constructor
    def __init__(self):
        self.transactions = []  # Initializes an empty transaction list for each account.

    def deposit(self, amount):
        """
            Creates a deposit transaction and adds it to the list of transactions.

            Parameters:
            amount(Decimal): The amount to be deposited, as a positive value.
        """

        #  Ensures that 'amount' is converted to a Decimal
        amount = Decimal(amount) if isinstance(amount, Decimal) else Decimal(str(amount))
        amount = abs(amount)  # Converts 'amount' to a positive value

        transaction = Transaction(amount)  # Creates Transaction instance
        self.transactions.append(transaction)  #  Appends instance to list of transactions

    def withdraw(self, amount):
        """
            Creates a 'withdraw' transaction and adds it to the list of transactions.

            Parameters:
            amount(Decimal): The amount to be withdrawn, as a negative value.
        """

        #  Ensures that 'amount' is converted to a Decimal
        amount = Decimal(amount) if isinstance(amount, Decimal) else Decimal(str(amount))
        amount = -abs(amount)  # Converts 'amount' to a negative value

        transaction = Transaction(amount)  # Creates Transaction instance
        self.transactions.append(transaction)  #  Appends instance to list of transactions

    def get_balance(self):
        """Returns the sum of all transactions stored on the Account object."""

        balance = 0  #  Sum of each transaction instance, initialized as 0

        for transaction in self.transactions:  #  Iterates over each transaction
            balance += transaction.amount  #  Amount of each transaction added to balance

        return balance  #  Returns the sum of each transaction

#  Code for the Transaction class

class Transaction:
    """
    A class representing a deposit or withdrawal from an account.

    Attributes:
        amount (Decimal): The amount of the transaction.

        timestamp (datetime): The date and time when the transaction occurred.
            Set to current date and time if no timestamp is provided.
    """

    #  Transaction class constructor
    def __init__(self, amount, timestamp=None):
        #  Ensures that 'amount' is converted to a Decimal
        self.amount = Decimal(amount) if isinstance(amount, Decimal) else Decimal(str(amount))

        #  Sets timestamp to current date and time if no argument is entered
        self.timestamp = timestamp or datetime.datetime.now()

    #  String representation for copying and pasting code
    def __repr__(self):
        #  Returns string representation of Transaction instance for coding
        return f"Transaction({self.amount}, {self.timestamp!r})"

    #  User-friendly string representation
    def __str__(self):

        #  Returns user-friendly string representation
        if self.amount > 0:
            #  Representation of deposits
            return f"{self.timestamp.strftime('%Y-%m-%d')}: +${self.amount:,.2f}"

        #  Representation of withdrawals
        return f"{self.timestamp.strftime('%Y-%m-%d')}: -${abs(self.amount):,.2f}"
