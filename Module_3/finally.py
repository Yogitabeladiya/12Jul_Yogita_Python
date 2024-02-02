try:
    a=int(input("enter a "))
    b=int(input("enetr b"))
    print("sum",a+b)
except:
    print("Error")
finally:# is optional
    print("this is finally block!")