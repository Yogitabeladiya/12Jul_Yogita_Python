fnm=input("enter first name")
lnm=input("enter last name")

if fnm.isupper() and lnm.isupper():
  

  email=input("enter your email")
  phone=input("entr you phone number")
  if email.islower() and len(phone)==0:
     print("fnm is ",fnm)
     print("lnm is ",lnm)
     print("email is",email)
     print("phone is",phone)
  else:
    print("proer details")
  passwod=input("enter your password")
  rpasswod=input("enter your re password")

  if passwod==rpasswod:
     print("password is",passwod)
  else:
     print("doen't match")
else:
   print("valid name")

