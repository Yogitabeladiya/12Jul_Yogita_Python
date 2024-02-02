
# single inheritance 
class father:
    car=0
    bal=0

    def getdata(self):
        self.car=input("Enter car details ")
        self.bal=input("Enter balance details ")

class son(father):
    def printdata(self):
        print("Car",self.car)
        print("Balance",self.bal)

s=son()
s.getdata()
s.printdata()


