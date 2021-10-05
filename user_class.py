#create user class 
class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

#creating a make_deposit method for my objects
    def makeDeposit(self, amount):
        self.amount += amount

#creating a withdrawal class
    def makeWithdrawal(self, amount):
      self.amount -= amount

# add method to display balance
    def displayBalance(self):
      print(f"User: {self.name}, Balance: {self.amount}")
        
#adding a transfer method to let one user transfer to another
    def transferAmount(self, amount, user):
      self.amount -= amount
      user.amount += amount
      self.displayBalance()
      user.displayBalance()





#instantiating instances to create new objects
Debbie = User("Debbie")
Josh = User("Josh")
Chi = User("Chi")

#Debbie makes 3 different deposits & 1 withdrawal 
Debbie.makeDeposit(100)
Debbie.makeDeposit(300)
Debbie.makeDeposit(300)
Debbie.makeWithdrawal(200)

#to show our current balance
Debbie.displayBalance()

#Josh makes 2 different deposits & 2 withdrawals 
Josh.makeDeposit(300)
Josh.makeDeposit(800)
Josh.makeWithdrawal(490)

Josh.displayBalance()

#Chi makes 1 different deposits & 3 withdrawals 
Chi.makeDeposit(600)
Chi.makeWithdrawal(90)
Chi.makeWithdrawal(79)
Chi.makeWithdrawal(200)

Chi.displayBalance()


#making a transfer to another user
Josh.transferAmount(200, Debbie)


