
class Bank_Customer:
    customer_counter = 0

    def __init__(self, name, customerID):
        Bank_Customer.__class__.customer_counter += 1
        self.name = name
        self.customerID = 10000 + customer_counter
        self.accounts = set()

class Account:
    account_counter = 0

    def __init__(self, Bank_Customer):
        self.__class__.account_counter = 0
        self.accountID = Bank_Customer.customerID + "-"
        self.account_owner = Bank_Customer
        self.balance = 0

    # def withdraw(self, amount, account):
    #     if self.account == account:
    #         self.balance = self.balance + amount
    #         return self.balance
    #
    # def deposit(self, amount, account):
    #     if self.account == account:
    #         self.balance = self.balance + amount


# class Savings_Account(Account):
#
#     def __init__(self, accountID):
#         super().__init__(accountID)
#
#
# class Childrens_Account(Account):
#     def __init__(self, accountID):
#         super().__init__(accountID)
#
#
# class Overdraft_Account(Account):
#     def __init__(self, accountID):
#         super().__init__(accountID)
