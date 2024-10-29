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

from banking import Account

def test_initialization():
    """Test that account object is initialized with transactions attribute"""
    test_account = Account()  #  Account object initialized for testing
    assert not test_account.transactions  #  Returns True if transactions[] is empty
