class grandfather:
    gold=0
    house=0

    def g_getdata(self):
        self.gold=input("Enter GOld Detiles")
        self.house=input("Enter House Detils ")
class father(grandfather):
    car=0
    bal=0

    def F_getdata(self):
        self.car=input("Enter Car Deteils")
        self.bal=input("Enter balance Deteils")

class son(father):
    def printdata(self):
        print("gold:",self.gold)
        print("house:",self.house)
        print("car:",self.car)
        print("bal:",self.bal)
s=son()
s.g_getdata()
s.F_getdata()
s.printdata()
