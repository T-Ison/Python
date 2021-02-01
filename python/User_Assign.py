class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        print(f'Depositing ${amount} to {self.name} acount.')
        return self
    
    def make_withdrawal(self,amount):
        print(f'Withdrawing ${amount} from {self.name} acount.')
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name} - ${self.account_balance} in their account\n")
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

john = User('John',"email@fake.com")
guido = User('Guido',"iMadePython@fake.com")
christine = User('Christine',"graham@email.com")

john.make_deposit(40).make_deposit(49).make_deposit(25).make_withdrawal(20).display_user_balance()
guido.make_deposit(50).make_deposit(60).make_withdrawal(20).make_withdrawal(40).display_user_balance()
christine.make_deposit(150).make_withdrawal(25).make_withdrawal(25).make_withdrawal(50).display_user_balance()
john.transfer_money(christine,44).display_user_balance()
christine.display_user_balance()