'''n=int(input("enter number "))
f=1
for i in range(n,1,-1):
    f=f*i
    print(f)
'''

# sum of averege 

'''n=int(input("enter number"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
av=sum/n
print(av)
'''


# privous number
privous_num=0
for i in range(1,11):
   x_sum=privous_num + i
   print("current number",i,"privious num",privous_num,"sum:",x_sum)
   privous_num+=1



