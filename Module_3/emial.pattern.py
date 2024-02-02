'''import re
email="yogita@gmail.com"
email_pattern="^[a-z]+[@]+[a-z]+[\.]+[a-z]"
x=re.findall(email_pattern,email)


if x:
    print("email is valid")
else:
    print("invalid")
'''

'''import re
n=input("Enter email")
e_p="^[a-z0-9]+[@]+[a-z]+[\.]+[a-z]"
x=re.findall(e_p,n)

if x:
    print("Valid")
else:
    print("Invalid ")
'''
import re

pas=input("Enter password")
r_pp="^[a-zA-Z0-9]"
x=re.findall(r_pp,pas)

if x:
    print("done")
    rp=input("Enter re password")
    r_pp="^[a-zA-Z0-9]"
    x1=re.findall(r_pp,rp)

    if x==x1:
        print("match")
    else:
       print("not  match ")
    
else:
    print("not done")


