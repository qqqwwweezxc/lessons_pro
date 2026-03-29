class BankAccount:
    """Class representing a bank account for working with banking transactions"""
    
    def __init__(self, balance: float = 0) -> None:
        """Initialize account balance"""
        self._balance = balance

    def deposit(self, amount: float):
        """Deposit amount to account"""
        if amount <= 0:
            raise ValueError("Amount must be a positive!")
        self._balance += amount
        print(f"You successfully deposited {amount} to your account. Balance: {self._balance}")
    
    def withdraw(self, amount: float):
        """Withdraw amount from account"""
        if amount <= 0:
            raise ValueError("Amount must be a positive!")
        elif self._balance < amount:
            raise ValueError("Not enough money on account")
        self._balance -= amount
        print(f"You successfully withdrawn {amount} from your account. Balance: {self._balance}")

    def get_balance(self) -> float:
        return self._balance
    
    

