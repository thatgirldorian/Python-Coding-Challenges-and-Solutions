class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.account = bankAccount(interest_rate=0.01, balance=0)

    def make_deposit(self, amount):
        account_type = input("\nWhat account are you depositing to?\n") 
        self.account.deposit(amount)
        print(f" {self.account.balance} has been deposited into your {account_type} account")
        return self

    def make_withdrawl(self,amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

#create bankAccount class
class bankAccount:

  def __init__ (self, interest_rate, balance):
    self.interest_rate = 0.01
    self.balance = 0
    

  #add a deposit method
  def deposit(self, amount):
    self.balance += amount
    return self

  #withdraw method
  def withdraw(self, amount):
    self.balance -= amount
    if self.balance < 1:
      self.balance -= 5
      print(f"Insufficient funds: Charging a $5 fee")
      return self
    

  def displayAccountInfo(self):
    print(f"Account Balance: ${self.balance}, Interest Rate: {self.interest_rate}")
    return self

  def yieldInterest(self):
    self.interest_rate = self.balance * self.interest_rate
    return self


adrien = User("Adrien")
nibbles = User("Mr. Nibbles")
benny_bob = User("Benny Bob")

adrien.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawl(45).display_user_balance()

nibbles.make_deposit(1000).make_deposit(1000).make_withdrawl(500).make_withdrawl(300).display_user_balance()

benny_bob.make_deposit(1500).make_withdrawl(1000).make_withdrawl(5000).make_withdrawl(3000).display_user_balance()


nibbles.transfer_money(400, adrien)



#creating instances
Debbie = User("Debbie")
Josh = User("Josh")

#Making 3 deposits & 1 withdrawal for first user
Debbie.make_deposit(700).make_deposit(280).make_deposit(410).make_withdrawl(80)

Debbie.account.yieldInterest()
Debbie.account.displayAccountInfo()

#Making 2 deposits & 4 withdrawals for second user
Josh.make_deposit(1800).make_deposit(2080).make_withdrawl(80).make_withdrawl(48).make_withdrawl(47).make_withdrawl(52)

Josh.account.yieldInterest()
Josh.account.displayAccountInfo()







