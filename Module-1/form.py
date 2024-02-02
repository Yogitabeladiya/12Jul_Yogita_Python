
fnm=input("enter name")
lnm=input("enter last name")
email=input("enter email")
mno=input("enter mno")
psd=input("enter password")
rpswd=input("enter repassword")


if fnm.isupper() and lnm.isupper():
    print(fnm)
    print(lnm)
else:
    print("enter in upercase")
if email.islower() and len(mno)==10:
    print(email)
    print(mno)
else:
     print("plz enter proper email and mno")
if psd==rpswd :
      print(psd)
else:
   print("does not match pass")
