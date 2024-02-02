#write a python program how to insert middle string  
'''str=input("enter string ")
print(str)
mid_str=" new "
temp=str.split()
mid_pos=len(temp)//2
res=(temp[:mid_pos]+[mid_str]+temp[mid_pos:])
print(' '.join(res))'''



string=input("enter string ")
print(string )

mid=input("what you can add in the mid ")
temp=string.split()
pos=len(temp)//2
res=(temp[:pos]+[mid]+temp[pos:])
print(' '.join(res))

