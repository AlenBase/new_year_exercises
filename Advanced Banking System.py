from abc import ABC, abstractmethod
from datetime import datetime

class Account(ABC):
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    @abstractmethod
    def display_balance(self):
        pass

class IndividualAccount(Account):
    def display_balance(self):
        return f"Account Type: {self.account_type}, Account Number: {self.account_number}, Balance: {self.balance}"

class JointAccount(Account):
    def display_balance(self):
        return f"Joint Account Type: {self.account_type}, Account Number: {self.account_number}, Balance: {self.balance}"

class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def view_accounts(self):
        return [account.display_balance() for account in self.accounts]

class Transaction:
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def execute(self):
        if self.transaction_type == "deposit":
            self.account.balance += self.amount
        elif self.transaction_type == "withdrawal":
            if self.account.balance >= self.amount:
                self.account.balance -= self.amount
            else:
                return "Insufficient funds"
        else:
            return "Invalid transaction type"

        return f"Transaction successful. New balance: {self.account.balance}"

individual_account = IndividualAccount(account_number="114561", balance=35000, account_type="Checking")
joint_account = JointAccount(account_number="598462", balance=10000, account_type="Savings")

customer = Customer(name="Artyom", contact_info="555-741-6953")
customer.add_account(individual_account)
customer.add_account(joint_account)

print(customer.view_accounts())

transaction = Transaction(account=individual_account, amount=1000, transaction_type="deposit")
print(transaction.execute())

transaction = Transaction(account=individual_account, amount=3000, transaction_type="withdrawal")
print(transaction.execute())

print(customer.view_accounts())
