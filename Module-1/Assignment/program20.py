# replace as good 
n=input("enter string")
snot=n.find('not')
spoor=n.find('poor')

if spoor>snot and snot>0 and spoor>0:
    print(n.replace(n[snot:(spoor+4)],'good'))
else:
    print(n)
