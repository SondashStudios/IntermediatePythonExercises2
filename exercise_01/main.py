# Developer: Caius Iliesi
# Date: 1/30/2024

from BankAccount import BankAccount

# Instantiate BankAccount with hardcoded values
account_name = "Caius"
starting_balance = 70.159
bank_account = BankAccount(account_name, starting_balance)

# Print the result of get_balance method
print(bank_account.get_balance())

