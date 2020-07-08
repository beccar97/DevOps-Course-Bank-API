"""Unit tests for bank.py"""

import pytest

from bank_api.bank import Bank, Account


@pytest.fixture
def bank() -> Bank:
    return Bank()


def test_accounts_are_immutable():
    account = Account('Immutable')
    with pytest.raises(Exception):
        # This operation should raise an exception
        account.name = 'Mutable'


def test_bank_creates_empty(bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0


def test_can_create_and_get_account(bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'


def test_cannot_duplicate_accounts(bank):
    bank.create_account('duplicate')
    bank.create_account('duplicate')

    assert len(bank.accounts) == 1


def test_cannot_modify_accounts_set(bank):
    accounts = bank.accounts
    accounts.add(Account('New Account'))

    assert len(bank.accounts) == 0


# TODO: Add unit tests for bank.add_funds()
def test_can_add_funds(bank):
    bank.create_account('Test')
    
    bank.add_funds('Test', 10)
    transaction = list(bank.transactions)[0]

    assert len(bank.transactions) == 1
    assert transaction.account == Account('Test')
    assert transaction.amount == 10

def test_can_add_negative_funds(bank):
    bank.create_account('Test')
    
    bank.add_funds('Test', -10)
    transaction = list(bank.transactions)[0]

    assert len(bank.transactions) == 1
    assert transaction.account == Account('Test')
    assert transaction.amount == -10

def test_cannot_add_decimal_funds(bank):
    bank.create_account('Test')
    
    with pytest.raises(ValueError):
        bank.add_funds('Test', 3.14)

def test_cannot_add_funds_to_non_existing_account(bank):
    with pytest.raises(ValueError):
        bank.add_funds('Test', 3.14)
