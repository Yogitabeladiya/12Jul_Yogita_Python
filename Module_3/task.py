
import random
x=random.randrange(11111,99999)
f1=open("yogi.txt","r+")

class Bank:
 
  
 def __init__(self):
  
    self.bal=0 
    self.bal=int(input("Enter Balance "))
  
 def Ac_user(self):
    self.name=input("Enter name")
    self.bal=int(input("Enter Balance "))
    if self.bal>=2500:
      print(self.bal)
    else:
      print("not sufficient")
    print("1.saving")
    print("2.Current")
    self.type=input("Enter Account type choice ")
    if self.type=='saving':
      print("Saving")
    elif self.type=='current':
     print("current")
    else:
      print("not avialble ")
    f1.write(f"name:-{self.name}\n Balance:-{self.bal}\n Type:-{self.type}\n Accountanumber:-{x}\n")

 def Deposite(self):
  self.amount=int(input("Enter deposite"))
  self.bal+=self.amount
  print("Deposite amount ",self.bal)
  f1.write(f"Deposite{self.bal}")

 def Withdraw(self,):
   self.withdra=int(input("Enter amonut Withdraw "))
   if self.bal>=self.withdra:
     self.bal-=self.withdra
     print("withdrwa mines ",self.bal)
     f1.write(f"Withdrwa{self.bal}")
   else:
     print("insufficient") 
   
 def print(self):
   print(f1.read())
   print("---------------------------")


b=Bank()



print("1.A/c open")
print("2.Deposite")
print("3.Withdraw")
print("4.Statement")


ch=input("enter user choice")
if ch=='1':
    b.Ac_user()

elif ch=='2':
    b.bal
    b.Deposite()
    
elif ch=='3':
    b.bal
    b.Withdraw()
  
else:
   b.print()







'''
class Atm:
    def __init__(self): # constructor is special method its call when class object cretaed 
        self.pin=''
        self.balance=0

        self.menu()


    def menu(self):
        user_input=input("""
                Hello how would you like to process 
                1.Enter 1 to Create pin
                2.Enter 2 to deposite
                3.Enter 3 to withdraw
                4.Enter 4 to cheak balance
      
""") 
        if user_input=="1":
             self.Create_pin()
        elif user_input=="2":
            self.Create_pin()
            self.deposite()
        elif user_input=="3":
            self.Create_pin()
            self.balance
            self.withdraw()
        elif user_input=="4":
            print("cheak balance")
        else:
            print("bye")


    def Create_pin(self):
        self.pin=input("Enter your pin")
        print(self.pin)
        #print("pin set")

    def deposite(self):
        temp=input("Enter your pin for deposite")
        if temp==self.pin:
            amount=int(input("Enter amount"))
            self.balance=self.balance+amount
            print("Deposite sucessfully")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp=input("Enter pin for withdraw")
        if temp==self.pin:
            amount=int(input("Enter amount for withdraw"))
            if amount<self.balance:
             self.balance=self.balance-amount
             print("withdraw sucessfully")
            else:
                print("insuffiecient balance")
        else:
            print("Invalid pin ")
   

    def cheak_balance(self):
        temp=input("Enter pin for cheak balance ")
        if temp==self.pin:
            print("balance",self.balance)
        else: 
            print("invalid pin")
        
sbi=Atm() 

'''
