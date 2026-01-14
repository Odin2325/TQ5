class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds")

        self.balance -= amount

    def transfer_to(self, other: "BankAccount", amount: float) -> None:
        if not isinstance(other, BankAccount):
            raise TypeError("Transfer target must be a BankAccount")

        self.withdraw(amount)
        other.deposit(amount)
