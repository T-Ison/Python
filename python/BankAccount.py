class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

class BankAccount:
    def __init__(self):
        self.account_balance = 0
        self.interest = 0.02

    def make_deposit(self, amount):
        self.account_balance += amount
        print(f'Depositing ${amount} to account.')
        return self
    
    def make_withdrawal(self,amount):
        if amount > self.account_balance:
            self.account_balance -= 5
            print("Insufficient funds: Charging a $5 fee")
            return self
        print(f'Withdrawing ${amount} from account.')
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"${self.account_balance} in their account\n")
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance = self.account_balance + (self.account_balance * self.interest)
        return self

Tom = User('Tom', 'Fake@mail.com')
Christine = User (name = 'Christine', email = 'Mail@fake.com')

Tom.account.make_deposit(1000).make_deposit(500).make_deposit(500).yield_interest().display_user_balance()
Christine.account.make_deposit(2000).make_deposit(2000).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200).yield_interest().display_user_balance()