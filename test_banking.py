"""
Python Development II
Assignment 5 - OOP Bank Account
Test Suite for banking.py module
John O.
October 31, 2024

This is a test suite for the banking.py module which tests its
properties and methods.

Usage:
Run this test module using pytest.

Imports:
    banking: Used for accurate representation of dollar values.
    datetime: Provides date and time for transaction timestamps.

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html

"""

import datetime
from banking import Account, Transaction


def test_initialization():
    """Test that account object is initialized with transactions attribute"""
    test_account = Account()  #  Account object initialized for testing

    #  Returns True if transactions[] is empty
    assert not test_account.transactions

def test_amount():
    """Test that the 'amount' parameter of 'Transaction' class is bound to self"""
    sample_amount = 100  #  Value to be added to 'amount' parameter
    test_transaction = Transaction(sample_amount)  #  Transaction object initialized

    #  Returns True if 'sample_amount' is the same as 'amount' property in 'test_transaction'
    assert sample_amount == test_transaction.amount

def test_timestamp_with_argument():
    """Tests that 'timestamp' in 'Transaction' class is bound to self with argument entered"""
    test_date = datetime.datetime(2024,1,1)  # Added to 'timestamp' parameter
    test_transaction = Transaction(100,test_date)  #  Transaction object initialized

    #  Returns True if 'test_date' is the same as 'timestamp' property in 'test_transaction'
    assert test_date == test_transaction.timestamp

def test_timestamp_without_argument():
    """Tests that 'timestamp' in 'Transaction' class is bound to self with default timestamp"""
    test_transaction = Transaction(100)  #  Transaction object with no timestamp added

    #  Returns True if default 'timestamp' is the same as current date and time
    assert test_transaction.timestamp == datetime.datetime.now()
