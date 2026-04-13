class BankAccount :
    def __init__(self,name : str,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount : int):
        self.balance += amount
        print(f"{self.name} deposited {amount}")
    def withdraw(self,amount : int) :
        if amount > self.balance :
            print("insufficient balance")
        else :
            self.balance -= amount
            print(f"{self.name} you have withdrawn {amount}")
    def display_balance(self):
        print(f"{self.balance}")
b1 = BankAccount("hareesh",100000)
b1.deposit(100)
b1.withdraw(100)
b1.display_balance()

        