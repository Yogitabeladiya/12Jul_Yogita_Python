
# user input dictionary
'''d={}
n=int(input("enter nummber"))
for i in range(n):
    k=input("enter keys")
    v=input("enter values")
    d[k]=v
print(d)'''


# static keys but values is user input 

'''dict={}
k=['id','name','city']
for i in range(len(k)):
  v=input(f"enter a value of {k[i]} :")
  dict[k[i]]=v
#print(dict) 


'''

'''d={}
k=['id','name','city']
for i in range(len(k)):
  v=input(f"enter values of{k[i]} :")
  d[k[i]]=v
print(d)

'''
'''d={}
n=int(input("enter number"))
for i in range(n):
    k=input("enter keys")
    v=input("enter values")
    d[k]=v
print(i)'''

'''d={}
n=int(input("enter number of student"))
for i in range(n):
    k=input("enter keys")
    v=input("enter values")
    d[k]=v
print(d)
'''

'''dict={}
k=['id','name','city']
for i in range(len(k)):
  v=input(f"enter values {k[i]}")
  dict[k[i]]=v
print(dict)'''






#nested dictionary 
'''student_data={
    'yogi':{'rolno':1,'city':'rjk','sub':'python'},
    'r':{'rno':1,'city':'amd','sub':'java'}
}
print(student_data)
print(student_data['yogi'])
print(student_data['r'])
student_data['yogi']['phonenum']=9054264505
print(student_data)
print(student_data['yogi'].pop('phonenum'))cls

'''





'''dict={ "yogita":101, "rinku":23, "nena":1, "bhagvati":2
}
lst=sorted(dict.items(),key=lambda x:x[0])
print(lst)
'''


# reverse by key and value
'''dict={ "yogita":101, "rinku":23, "mital":21, "nena":1, "bhagvati":2}
for k,v in dict.items():
  print("origunal dict",dict)
for v,k in dict.items():
     print("after revese ",v,k)

'''