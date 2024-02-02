try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print("sum:",A+b)
except Exception as e :
    print(e)
else: 
    print("this is finally bloack!")