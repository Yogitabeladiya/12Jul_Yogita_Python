# if string is less 2 print first and last 2 charcter otherwise print string. 
mystr=input("enter string ")
if len(mystr)>=2:
    print(mystr[:2],mystr[-2:])
else:
    print(mystr)


    