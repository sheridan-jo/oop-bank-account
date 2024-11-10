"""
Python Development II
Assignment 5 - OOP Bank Account
Test Suite for banking.py module
John O.
November 10, 2024

This is a test suite for the banking.py module which tests its
properties and methods.

Usage:
Run this test module using pytest.

Imports:
    datetime: Provides date and time for transaction timestamps.
    Account: For testing deposit, withdraw, and balance retrieval
        methods and transactions property
    Transaction: For testing properties and methods of Transaction
        class.
    Decimal: Used for accurate representation of dollar values.

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html

"""

import datetime
from decimal import Decimal
from banking import Account, Transaction

#  Tests for Account

def test_initialization():
    """Test that account object is initialized with transactions attribute"""
    test_account = Account()  #  Account object initialized for testing

    #  Passes if transactions[] is empty
    assert not test_account.transactions

def test_deposit():
    """
    Test that the deposit method accepts an amount parameter,
    converts it to a positive value and creates a new
    instance of a Transaction appended to transactions list.
    """
    test_account = Account()  #  Account object initialized for testing

    test_account.deposit(-100)  #  Negative value enter for amount parameter

    #  Passes if the last transaction amount is stored as a positive Decimal value
    assert test_account.transactions[-1].amount == Decimal(100)

def test_withdraw():
    """
        Test that the 'withdraw' method accepts an amount parameter,
        converts it to a negative value and creates a new
        instance of a Transaction appended to transactions list.
    """

    test_account = Account()  # Account object initialized for testing

    test_account.withdraw(99.99)  #  Value for amount parameter

    #  Passes if the last transaction amount is stored as a negative Decimal Value
    assert test_account.transactions[-1].amount == Decimal('-99.99')

def test_get_balance_with_no_transactions():
    """Tests that 0 is returned if no transactions exist in an Account object"""

    test_account = Account()  #  Account object initialized for testing

    assert test_account.get_balance() == 0

def test_get_balance_with_transactions():
    """Tests that 'get_balance' returns the sum of all transactions"""

    test_account = Account()  #  Account object initialized for testing

    test_account.deposit(100)  #  Deposits 100 into the account
    test_account.withdraw(90)  #  Withdraws 90 from the account
    test_account.deposit(10)  #  Deposits 10 into the account

    #  Passes if the sum of all transactions is 20
    assert test_account.get_balance() == 20

#  Tests for Transaction

def test_amount():
    """Test that the 'amount' parameter of 'Transaction' class is bound to self"""
    sample_amount = 100  #  Value to be added to 'amount' parameter
    test_transaction = Transaction(sample_amount)  #  Transaction object initialized

    #  Passes if 'sample_amount' is the same as 'amount' property in 'test_transaction'
    assert sample_amount == test_transaction.amount

def test_timestamp_with_argument():
    """Tests that 'timestamp' in 'Transaction' class is bound to self with argument entered"""
    test_date = datetime.datetime(2024,1,1)  # Added to 'timestamp' parameter
    test_transaction = Transaction(100,test_date)  #  Transaction object initialized

    #  Passes if 'test_date' is the same as 'timestamp' property in 'test_transaction'
    assert test_date == test_transaction.timestamp

def test_timestamp_without_argument():
    """
    Tests that 'timestamp' in 'Transaction' class is bound to self with default timestamp.

    This test is designed to account for slight time delays between the current time
    and the time that the Transaction instance was created.
    """

    start_time = datetime.datetime.now()  #  Time before creating Transaction instance
    test_transaction = Transaction(100)  #  Transaction object initialized
    end_time = datetime.datetime.now()  #  Time after creating Transaction instance

    #  Passes if timestamp property is close to the current time
    assert start_time <= test_transaction.timestamp <= end_time

def test_repr():
    """Tests that repr method returns the expected string output"""
    sample_amount = 99.99  # Passed as argument for 'amount'

    #  Passed as argument for 'timestamp'
    test_timestamp = datetime.datetime(2024, 1, 1, 12, 0)

    #  Transaction instance for this test
    test_transaction = Transaction(sample_amount, test_timestamp)

    # The expected string output of the repr method
    expected_repr = "Transaction(99.99, datetime.datetime(2024, 1, 1, 12, 0))"

    #  Passes if repr method of test_transaction is the same as expected_repr
    assert repr(test_transaction) == expected_repr

def test_str_with_positive_amount():
    """Tests that str method returns the expected string output with a positive amount"""

    #  Passed as argument for 'timestamp'
    test_timestamp = datetime.datetime(2024, 1, 1, 12, 0)

    #  Transaction instance for this test
    test_transaction = Transaction(1234.56, test_timestamp)

    #  Expected output for str method
    expected_str = "2024-01-01: +$1,234.56"

    #  Passes if str method of test_transaction is the same as expected_str
    assert str(test_transaction) == expected_str

def test_str_with_negative_amount():
    """Tests that str method returns the expected string output with a negative amount"""

    #  Passed as argument for 'timestamp'
    test_timestamp = datetime.datetime(2024, 1, 1, 12, 0)

    #  Transaction instance for this test
    test_transaction = Transaction(-1234.56, test_timestamp)

    #  Expected output for str method
    expected_str = "2024-01-01: -$1,234.56"

    #  Passes if str method of test_transaction is the same as expected_str
    assert str(test_transaction) == expected_str
