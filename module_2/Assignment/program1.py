# largest number ,smallest number and sum

'''def largest():
 list=[2,3,4,5,1]
 print(max(list))
 print(min(list))
 print(sum(list))
largest()

'''

'''def largest():
    list=[1,4,2,3,5]
    max=list[0]
    for x in list:
        if x>max:
            max=x
    return max
print(largest())

''' 
# sort list
'''list=[5,8,6,4,1,0]
n=len(list)
for i in range(n):
    for j in range(i+1,n):

        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)

'''

#fiboo
'''def fiboo():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

f1=fiboo()

print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))'''


# palindriom

'''string=input("enter string ")
st=string[::-1]
if st==string:
    print("palindrom")
else:
    print("not palindrom ")
'''

# sort dict

'''dict1={575:'mangoes',452:'apple',678:'banana',453:'stobery',123:'gvava'}

d=sorted(dict1.items())
print(dict(d))'''

'''dict1={575:'mangoes',452:'apple',678:'banana',453:'stobery',123:'gvava'}
d=sorted(dict1.keys())

dict2={}
for i in d:
    dict2[i]=dict1[i]

print(dict2)
'''

#Dict comphersion 
'''dict1={575:'mangoes',452:'apple',678:'banana',453:'stobery',123:'gvava'}
dict2={k:v for k,v in sorted (dict1.items(), key=lambda x:x[0])}

print(dict2)
'''

#the sky is blue
#blue is sky the 


'''s="the sky is blue"
l=s.split()
l=l[::-1]
l=' '.join(l)
print(l)
'''

# min and max

'''l=[1,7,8,4,5,223,112,0]
minimum=l[0]
maximum=l[0]

for i in l:
    if i<minimum:
        minimum=i
    if i>maximum:
        maximum=i
print("minum",minimum)
print("maximum",maximum)
'''

