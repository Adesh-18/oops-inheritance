# encapsulation means:
# keeps data and methods inside a class and controlling how that data is accessed or changed

3 # THINK ABOUT A BANK ACCOUNT 
'''
You should not directly change the balance like this:

account.balance = -100000

Instead, the class should control changes through methods such as:

account.deposit(1000)
account.withdraw(500)
'''
# Here, the data and methods are grouped inside one class.
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def show_balance(self):
        print(self.balance)
a1 = BankAccount(5000)
a1.deposit(1000)
a1.show_balance()

#access levels in python 
#public 
#protected
#private

# self.__balance

# Two underscores (__).

# This makes the attribute private.

class Bank:
    def __init__(self):
        self.__balance = 1000
    def show_balance(self):
        print(self.__balance)
acc = Bank()
acc.show_balance()
# now the user cannot change the method directly
# Encapsulation is the process of bundling data and methods together while restricting direct access to important data
# Data

# ↓

# Protect it

# ↓

# Allow access through methods

class Student:
    def __init__(self):
        self.__marks = 95
    def show_marks(self):
        print(self.__marks)
student = Student()
student.show_marks()
print(student_marks)