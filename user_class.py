# creating a class
class User:
  bank_name = "WEE National Bank"
  def __init__(self, name, email_address, deposit_amount, user_balance):
    self.name = name
    self.email = email_address
    self.deposit_amount = deposit_amount
    self.user_balance = user_balance

#creating a make_deposit method for my objects
  def makeDeposit(self):
    #Have the first user make 3 deposits and 1 withdrawal and then display their balance
    if self.deposit_amount >= 1:print(f"Hello, my name is {self.name} and I want to deposit {self.deposit_amount * 3}.") 
    else: return (self.deposit_amount)
    #printing to see if it works the way it should
    

#creating a method for withdrawal
  def makeWithdrawal(self):
    #printing to see if it works the way it should
    print(f"Hello, my name is {self.name} and I'd also like to withdraw {self.user_balance - 500}.")

  def displayUserBalance(self):
    #printing to see if it works the way it should
    print(f"Hello, my name is {self.name} and I currently have {self.user_balance} in my account.")

#instantainting an instance to create new object
user1 = User("John", "john@gmail.com", 500, 2000)
user1.makeDeposit()
user1.makeWithdrawal()
user1.displayUserBalance()

# #a few other instances of this class
# user2 = User("Debbie", "debbie@gmail.com", 900, 8000)

# user3 = User("Bola", "bola@gmail.com", 800, 5000)

# user4 = User("Osas", "osas@gmail.com", 600, 3000)


# #Have user 2 make three deposits, 1 withdrawal and then display their bank balance
# user2.makeDeposit()


