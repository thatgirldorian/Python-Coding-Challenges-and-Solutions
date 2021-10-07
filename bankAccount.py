#create bankAccount class
class bankAccount:

  def __init__ (self, name, interest_rate, balance):
    self.name = name
    self.interest_rate = 0.01
    self.balance = 0

#use a classmethod to print all instances of a Bank Account's info
  @classmethod
  def showBankInfo(cls, name, interest_rate, balance):
    print(name, interest_rate, balance)


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

