class BankAccount:
    bank_name = "Navy Dojo"
    bank_loc = "Los Angeles"
    def __init__(self, int_rate, balance):
        self.int_rate = 0.03
        self.balance = 0
        BankAccount.bank_name = "Wells fargo"


    def deposit(self, balance):
        self.balance += balance
        print(f"You have deposited {self.balance}")
        return self


    def withdraw(self, balance):
        self.balance -= balance
        if self.balance < balance:
            print(f"You have insufficient funds of -" + str(balance))
            charge = balance + 5
            deduct = balance - 5
            print(f"You are being charged for $5 " + "Your account is $ " + str(deduct) + " We will deduct $5, your account balance is " + str(deduct - 5))
            return self
        else:
            self.balance = balance
            print(f"You have withdrawn $ " + str(balance))
            return self

    def display_account(self):
        return self

    def yield_interest(self):
        calculatedInterest = self.int_rate * self.balance
        print(f"Your account interest is {self.int_rate} and your balance is {self.balance}")
        return self

    @classmethod
    def change_bank(cls):
            print(f"The name is: ", cls.bank_name)

    @classmethod
    def change_loc(cls):
        print(cls.bank_loc, "will be the nearest location")

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account = BankAccount(int_rate=0.02, balance=0)
        print(self.account.balance)





rodney = User(0.03, 500)
rodney.account.deposit(3300).deposit(500)
rodney.account.withdraw(500).withdraw(1000)
rodney.account.yield_interest()





selena = User(0.03, 1000)
selena.account.deposit(300).deposit(500).deposit(300).deposit(200).deposit(5000).withdraw(700)
print(f"Your account interest is {selena.account.int_rate} and you Selena has a balance of {selena.account.balance}")
selena.account.yield_interest()


ryan = User(0.03, 1000)
ryan.account.deposit(400).deposit(900).deposit(700).deposit(2000).withdraw(500)
print(f"Your account interest is {ryan.account.int_rate} and you Ryan has a balance of {ryan.account.balance}")
ryan.account.yield_interest()
