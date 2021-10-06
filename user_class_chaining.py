#create user class 
class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

#creating a make_deposit method for my objects
    def makeDeposit(self, amount):
        self.amount += amount
        return self
        

#creating a withdrawal class
    def makeWithdrawal(self, amount):
      self.amount -= amount

# add method to display balance
    def displayBalance(self):
      print(f"User: {self.name}, Balance: {self.amount}")
      return self
        
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

#Debbie makes 3 different deposits & 1 withdrawal + chaining all ou methods to save space
Debbie.makeDeposit(100).makeDeposit(300).makeDeposit(300).makeWithdrawal(200).displayBalance()


#Josh makes 2 different deposits & 2 withdrawals 
Josh.makeDeposit(300).makeDeposit(800).makeWithdrawal(490).displayBalance()

#Chi makes 1 different deposits & 3 withdrawals 
Chi.makeDeposit(600).makeWithdrawal(90).makeWithdrawal(79).makeWithdrawal(200).displayBalance()


#making a transfer to another user
Josh.transferAmount(200, Debbie)


