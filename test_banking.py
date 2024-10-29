"""
Python Development II
Assignment 5 - OOP Bank Account
Test Suite for banking.py module
John O.
October 29, 2024

This is a test suite for the banking.py module which tests its
properties and methods.

Usage:
Run this test module using pytest.

Documented according to Google Style Docstrings
https://google.github.io/styleguide/pyguide.html

"""

from banking import Account, Transaction

def test_initialization():
    """Test that account object is initialized with transactions attribute"""
    test_account = Account()  #  Account object initialized for testing

    #  Returns True if transactions[] is empty
    assert not test_account.transactions

def test_amount():
    """Test that the 'amount' parameter of 'Transaction' class is bound to 'self' """
    sample_amount = 100  #  Value to be added to 'amount' parameter
    test_transaction = Transaction(sample_amount)  #  Transaction object initialized

    #  Returns True if 'sample_amount' is the same as the 'amount' property in 'test_transaction'
    assert sample_amount == test_transaction.amount
