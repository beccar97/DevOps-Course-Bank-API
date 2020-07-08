from dataclasses import dataclass
from datetime import datetime
from typing import Set
from bank_api.bank import Bank

class BankReport:
    def __init__(self, bank: Bank):
        self._bank: Bank = bank

    def get_balance(self, account_name: str) -> int:
        """Gets the balance of the named account"""
        try:
            self._bank.get_account(account_name)
        except ValueError:
            raise
        
        return sum(trs.amount 
            for trs in self._bank.transactions 
            if trs.account.name == account_name
        )

