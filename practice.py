class Account:
    def __init__(self, balance, currency):
        self.balance = balance
        self.currency = currency
    
    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount
    
    # Method to withdraw money from the account (with exception handling for insufficient funds)
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise Exception("Insufficient funds during withdrawal.")
    
    # Overload the + operator to transfer money between accounts
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Mismatched currencies during transfer.")
        
        # Return a new Account object with combined balances
        return Account(self.balance + other.balance, self.currency)

# Derived class for SavingsAccount
class SavingsAccount(Account):
    def __init__(self, balance, currency, interest_rate):
        super().__init__(balance, currency)
        self.interest_rate = interest_rate
    
    # Apply interest to the account balance
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
    
    # Override the withdraw method to enforce a withdrawal limit of $2000 per transaction
    def withdraw(self, amount):
        if amount > 2000:
            raise Exception("Withdrawal limit of $2000 per transaction exceeded.")
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise Exception("Insufficient funds during withdrawal.")

# Derived class for CurrentAccount
class CurrentAccount(Account):
    def withdraw(self, amount):
        fee = 10
        if self.balance >= amount + fee:
            self.balance -= (amount + fee)
        else:
            raise Exception("Insufficient funds, including the withdrawal fee.")

# Test cases

# Create a SavingsAccount with $3000 balance and 5% interest rate
savings1 = SavingsAccount(3000, 'USD', 0.05)

# Create another SavingsAccount with $2000 balance and 3% interest rate
savings2 = SavingsAccount(2000, 'USD', 0.03)

# Deposit $1000 into the first savings account
savings1.deposit(1000)

# Try withdrawing $2500 from the first savings account (should raise an exception)
try:
    savings1.withdraw(2500)
except Exception as e:
    print(e)  # Withdrawal limit of $2000 per transaction exceeded.

# Apply interest to the second savings account
savings2.apply_interest()

# Create a CurrentAccount with $1500 balance
current = CurrentAccount(1500, 'USD')

# Try withdrawing $1500 (should fail due to insufficient funds including the $10 fee)
try:
    current.withdraw(1500)
except Exception as e:
    print(e)  # Insufficient funds, including the withdrawal fee.

# Transfer $500 from savings2 to savings1 (overloaded + operator)
try:
    new_account = savings1 + savings2
    print(f"New Account Balance: {new_account.balance}")
except Exception as e:
    print(e)



import os

# unpacking the tuple
file_name, file_extension = os.path.splitext("/Users/pankaj/abc.txt")

print(file_name)
print(file_extension)