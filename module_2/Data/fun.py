import random

def getdata():
        x=random.randint(111,999)
        name=input("enter name")
        nm1=name.upper()
        sub=input("enetr sub")
        city=input("enetr city")
        print(x)
        print(name)
        print(sub)
        print(city)
        list=[x,nm1,sub,city]        
        print(list)

def st():
        list=[]
        for i in range(5):
         x=random.randint(111,999)
         nm=input("enter name ")
         sub=input("enter sub ")
         city=input("enyter city")

         print("name",nm)
         nm1=nm.upper()
         print("subect",sub)
         print("city",city)
         a=[x,nm1,sub,city]
         list.append(a)
print(list)