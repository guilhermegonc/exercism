import threading


class BankAccount:
    def __init__(self, balance=0, status=False):
        self.balance = balance
        self.status = status
        self.lock = threading.Lock()

    def get_balance(self):
        if self.status:
            return self.balance
        raise ValueError

    def open(self):
        self.status = True
        pass

    def deposit(self, amount):
        if self.status and amount > 0:
            with self.lock:
                self.balance += amount
            return self.balance
        raise ValueError

    def withdraw(self, amount):
        if self.status and self.balance >= amount >= 0:
            with self.lock:
                self.balance -= amount
            return self.balance

        raise ValueError

    def close(self):
        self.status = False
        pass
