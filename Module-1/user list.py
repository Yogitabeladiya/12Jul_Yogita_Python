'''city=[]
n=int(input("enter number of city"))
for i in range(n):
    c=input("enter city")
    city.append(c)
    city.sort()
print(city)


'''
'''n=int(input("enter list of student "))
l=[]
for i in range(n):
    i=int(input("enter id "))
    s=input("enter subject ")
    c=input("enetr city")
    l.append(i)
    l.append(s)
    l.append(c)
print(l)
'''
n=int(input("Enter list of student"))
l=[]
for i in range(n):
    i=int(input("Enter id "))
    s=input("enter subject")
    c=input("enter city")
    list=[i,s,c]
    l.append(list)
print(l)