'''class yogita:
    yid=0
    ysub=''

    def y_getdata(self):
        self.yid=input("Enter Yogita's Id ")
        self.ysub=input("Enter Yogita's Subject")

class rinkal:
    rid=0
    rsub=''

    def r_getdata(self):
        self.rid=input("Enter Rinkal's Id ")
        self.rsub=input("Enter Rinkal's Subject ")


class tops(yogita,rinkal):
    def printdata(self):
        print("----------yogita's Data--------------------------")
        print(" Yogita's ID :",self.yid)
        print(" yogita's Subject",self.ysub)
        print("----------Rinkal's Data---------------------------")
        print(" Rinkal's Id ",self.rid )
        print(" Rinkal's Subject",self.rsub)

t=tops()
t.y_getdata()
t.r_getdata()
t.printdata()
 '''

class y1:
    Did=0
    Dnm=''
    def dog(self):
        self.Did=input("Enter Did")
        self.Dnm=input("Enter Dnm")


class y2(y1):
    Did1=0
    Dnm1=''

    def dog1(self):
        self.Did1=input("Enter dog id ")
        self.Dnm1=input("Enter dog name ")

class y3(y2):
    Did3=0
    Dnm3=''
    def dog2(self):
        self.Did3=input("Enter dog id")
        self.Dnm3=input("Enter dog name")

class y4(y3):
    def dog3(self):
        print("______________Dog Details____________")
        print("DOg1 id ",self.Did)
        print("Dog1 name",self.Dnm)
        print("------------Dog1 Details--------------")
        print("Dog2 Id",self.Did1)
        print("Dog2 name",self.Dnm1)
        print("_____________Dog2 Details_____________ ")
        print("DOg3 Id",self.Did3)
        print("Dog3 name",self.Dnm3)

d=y4()
d.dog()
d.dog1()
d.dog2()
d.dog3()
