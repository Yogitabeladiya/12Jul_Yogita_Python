# swap with temp variable and without variable 
'''a=int(input("enter value a"))
b=int(input("enter value b"))
temp=a
a=b
b=temp
print("a is ",a)
print("b is",b)
'''
# without temp 
'''a=int(input("enter value a"))
b=int(input("enter value b"))
a,b=b,a
print("a is ",a)
print("b is ",b)'''