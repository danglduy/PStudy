"""
Object-Oriented Banking: Design a banking system with classes for Account, Customer, and Transaction that handles deposits, withdrawals, and transfers.
"""

from uuid import uuid4

class Account:
    def __init__(self, account_id):
        self._balance = 0
        self.account_id = account_id
        self.transaction_log = []

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Account balance must be larger than or equal to 0")

        self._balance = value

    def deposit(self, transaction_id, value):
        if value < 0:
            raise ValueError("Cannot deposit a negative amount")

        self.balance += value
        self.transaction_log.append((transaction_id, 'deposit', value))

    def withdrawal(self, transaction_id, value):
        if value < 0:
            raise ValueError("Cannot withdrawal a negative amount")

        self.balance -= value
        self.transaction_log.append((transaction_id, 'withdrawal', value))

    def rollback(self, transaction_id):
        last_log = self.transaction_log[-1]

        if last_log[0] == transaction_id:
            last_action = last_log[1]
            if last_action == 'deposit':
                self.withdrawal(uuid4(), last_log[2])
            else:
                self.deposit(uuid4(), last_log[2])
        else:
            print(f"transaction no {transaction_id} does not present in account {self.account_id}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if not isinstance(account, Account):
            raise TypeError("Invalid account object type")
        self.accounts[account.account_id] = account


    def transfer(self, source_id, destination_id, value):
        if not (source_id in self.accounts) or not (destination_id in self.accounts):
            print(source_id)
            print(destination_id)
            print(self.accounts)
            raise ValueError('A account not present in our system')

        source = self.accounts[source_id]
        destination = self.accounts[destination_id]
        transaction_id = str(uuid4())

        try:
            source.withdrawal(transaction_id, value)
            destination.deposit(transaction_id, value)
        except Exception as e:
            print(f"Transfer failed: {e}. Rolling back")
            source.rollback(transaction_id)
            destination.rollback(transaction_id)

# Gonna skip Customer

account1 = Account('account1')
account2 = Account('account2')
bank = Bank()
bank.add_account(account1)
bank.add_account(account2)

account1.deposit('account11',100)
account2.deposit('account21',200)
bank.transfer(account1.account_id, account2.account_id, 50)

print(account1.balance) # should be 50
print(account2.balance) # should be 250

