# This page manages encapsulation.
class BankAccount:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self, amount):
        if self._balance > 0:
            self._balance += amount
            print(f"Your new balance is: {self._balance}")
            return True
        else:
            print("You don't have enough money")
            return False


my_account = BankAccount("majd", 5000)
my_account.deposit(1000)
