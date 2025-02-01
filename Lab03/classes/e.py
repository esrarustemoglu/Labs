class BankAccount():
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance
    def state(self):
        print(f"{self.owner}, you have {self.balance}$ in your account")
    def deposit(self, amount):
            self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance : {self.balance}")
        else:
            print("The amount you want to withdraw exceeds your current balance.")
account = BankAccount("Esra", 500)
account.state()
account.deposit(100)
account.withdraw(300)
account.state()
account.withdraw(400)