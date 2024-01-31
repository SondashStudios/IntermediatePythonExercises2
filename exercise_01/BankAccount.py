# Developer: Caius Iliesi
# Date: 1/30/2024

class BankAccount:
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    def deposit(self, amount):
        # Add the deposit amount to the balance
        self.balance += amount

    def withdraw(self, amount):
        # Check if withdrawal amount is valid
        if amount < 0:
            print("Invalid withdrawal amount.")
            return

        # Check if there are sufficient funds
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            # Subtract the withdrawal amount from the balance
            self.balance -= amount

    def get_balance(self):

        formatted_balance = "${:.2f}".format(self.balance)
        return f"{self.account_name} has a balance of {formatted_balance}"

