"""Unit tests for bank.py"""

import pytest

from bank_api.bank import Bank, Account
from bank_api.bank_report import BankReport

account_name = 'test'

@pytest.fixture
def bank() -> Bank:
    bank = Bank()
    bank.create_account(account_name)
    return bank


@pytest.fixture
def bank_report(bank) -> BankReport:
    return BankReport(bank)


def test_can_get_empty_account_balance(bank_report):
    balance = bank_report.get_balance(account_name) 
    assert balance == 0


def test_can_get_positive_account_balance(bank, bank_report):
    bank.add_funds(account_name, 100)
    balance = bank_report.get_balance(account_name)
    assert balance == 100


def test_cannot_get_account_balance_if_account_does_not_exist(bank_report):
    with pytest.raises(ValueError):
        bank_report.get_balance('invalid')
