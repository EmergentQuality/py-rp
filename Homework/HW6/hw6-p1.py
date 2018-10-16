"""Script which defines a BankAccount class.
Jeffrey Liss
This is a god-awful mess, but it's as far as I was able to get.
"""


class BankAccount:

    """ A standard account and methods to deposit and withdraw funds and to add
    interest.
    """

    def __init__(self):
        """ Creates the BankAccount with a starting balance of $0 and the
        standard interest rate. """
        self.balance = 0
        self.interest_rate = 2.0

    def __str__(self):
        return f'A {self.__class__.__name__} with a balance of:${self.balance}'

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.balance!r}, {self.interest_rate!r})')

    def get_balance(self, account):
        """Returns the account balance as a float"""
        return format(self.balance, '2g')

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance = self.balance + deposit_amount
            print(
                f"Deposited ${deposit_amount}. Your balance is ${self.balance}"
            )
            return self.balance
        else:
            print("Invalid deposit amount.")
            return False

    def withdraw(self, withdraw_amount):
        if self.balance > withdraw_amount:
            self.balance = self.balance - withdraw_amount
            return withdraw_amount
        else:
            print("Insufficient funds.")
            ovrd_acct = OverdraftAccount()
            return False

    def accumulate_interest(self):
        if self.balance <= 0:
            return False
        else:
            self.balance = self.balance + \
                ((self.balance * self.interest_rate) / 100)
            print("Applied interest. New balance is: ${}".format(self.balance))


class ChildrensAccount(BankAccount):

    def __init__(self):
        super().__init__(self)
        self.interest_rate = None

    def accumulate_interest(self):
        self.balance += 10


class OverdraftAccount(BankAccount):

    def __init__(self):
        self.balance = 40.
        super().__init__(self)


class BankTransaction:
    def __init__(self, source_account, target_account, transfer_amount=0,):
        self.source_account = source_account
        self.target_account = target_account
        self.transfer_amount = transfer_amount

    def transfer_funds(self):
        if self.source_account.balance >= self.transfer_amount:
            self.source_account.withdraw(self.transfer_amount)
            self.target_account.deposit(self.transfer_amount)
            print(
                f"Transfered ${self.transfer_amount} from {self.source_account} to {self.target_account}")
        else:
            print("Insufficient funds.")


myaccount = BankAccount()
bel_account = ChildrensAccount()
myaccount.deposit(5000)
myaccount.accumulate_interest()
bel_account.accumulate_interest()
print(myaccount.balance)
print(bel_account.balance)
transaction1 = BankTransaction(myaccount, bel_account, 500)
transaction1.transfer_funds()
print(myaccount.balance)
transaction2 = BankTransaction(myaccount, bel_account, 300)
transaction2.transfer_funds()
print(bel_account.balance)
