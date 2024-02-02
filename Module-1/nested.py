'''s1=int(input("enter subject1: "))
s2= int(input("enter subject2: "))
s3=int(input("enter subject3  :"))
s4=int(input ("enter subject4 :"))

if s1>=40 and s2>=40 and s3>=40 and s4>=40:
    total=s1+s2+s3+s4
    print(total)

    pr=total/4
    print(pr)

    if pr>=70:
        print("dist")
    elif pr>=60:
        print("first class")
    elif pr>=50:
        print("second class")
    elif pr>=40:
        print("pass class")
else:
    print("fail")
'''
     
'''s1=int(input("enter subject"))
s2=int(input("enter subject"))
s3=int(input("enter subject"))
s4=int(input("enter subject"))


if s1>=40 and s2>=40 and s3>=40 and s4>=40:
    total=s1+s2+s3+s4
    print(total)

    pr=total/4
    print(pr)


    if pr>=70:
        print("dist")
    elif pr>=60:
        print("first class")
    elif pr>=50:
        print("second class")
    elif pr<=40:
        print("pass")

else:
    print("fail")

    
'''

'''import sqlite3

con=sqlite3.connect("test.db")
con.execute()
print("connetted")'''


