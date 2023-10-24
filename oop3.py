class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited Ksh{amount}. New balance: Ksh{self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew Ksh{amount}. New balance: Ksh{self.balance}"
        else:
            return "Insufficient funds."

    def get_balance(self):
        return f"Account #{self.account_number} balance: Ksh{self.balance}"


# Create a bank account
account1 = BankAccount(12345)

print(account1.deposit(1000))
print(account1.withdraw(500))
print(account1.get_balance())