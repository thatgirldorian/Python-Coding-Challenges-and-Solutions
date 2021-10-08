#create bankAccount class
class bankAccount:

  def __init__ (self, name, interest_rate, balance):
    self.name = name
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
    print(f"User: {self.name}, Account Balance: ${self.balance}, Interest Rate: {self.interest_rate}")
    return self

  def yieldInterest(self):
    self.interest_rate = self.balance * self.interest_rate
    return self

#creating instances
Debbie = bankAccount("Debbie", 0, 0)
Josh = bankAccount("Josh", 0, 0)

#Making 3 deposits & 1 withdrawal for first user
Debbie.deposit(700).deposit(280).deposit(410).withdraw(80)

Debbie.yieldInterest()
Debbie.displayAccountInfo()

#Making 2 deposits & 4 withdrawals for second user
Josh.deposit(1800).deposit(2080).withdraw(80)
Josh.withdraw(48)
Josh.withdraw(47)
Josh.withdraw(52)

Josh.yieldInterest()
Josh.displayAccountInfo()






class User:

    def __init__(self, name, account):
        self.name = name
        self.amount = 0
        self.account = bankAccount(interest_rate=0.01, balance=0)

    def make_deposit(self, amount):
        self.account.make_deposit(100)

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


adrien = User("Adrien", 0)
nibbles = User("Mr. Nibbles")
benny_bob = User("Benny Bob")

adrien.make_deposit(100)
adrien.make_deposit(200)
adrien.make_deposit(50)
adrien.make_withdrawl(45)
adrien.display_user_balance()

nibbles.make_deposit(1000)
nibbles.make_deposit(1000)
nibbles.make_withdrawl(500)
nibbles.make_withdrawl(300)
nibbles.display_user_balance()

benny_bob.make_deposit(1500)
benny_bob.make_withdrawl(1000)
benny_bob.make_withdrawl(5000)
benny_bob.make_withdrawl(3000)
benny_bob.display_user_balance()


nibbles.transfer_money(400, adrien)



