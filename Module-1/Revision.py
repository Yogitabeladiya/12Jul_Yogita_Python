# number positive or negative or zero 

'''n=int(input("enter number"))

if n>0:
    print("positive number")
elif n<0:
    print("negative")
else:
    print("zero")'''

# fact

'''n=int(input("enter number "))
sum=1
for i in range(n,1,-1):
    sum=sum*i
print(sum)
'''

# fiboo

'''n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    '''

# fiboo 
'''def fiboo(n):
    a,b=0,1
    print("fibo",a)
    print("fibo",b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print("fiboo",c)
fiboo(10)
'''


# swap with temp and without temp

'''a=int(input("enter a number"))
b=int(input("enter b number "))


print("before swap",a)
print("before swap",b)


a,b,=b,a

c=a
a=b
b=c

print("after swap",a)
print("after swap",b)
'''

# number even or odd

'''n=int(input("enter n "))

if n%2==0:
    print(f"number is {n} even ")
else:
    print(f"number is {n} odd")
'''

'''list1=['a','i','o','u','e','A','E','O','U','I']
v=input("enter letter")

if v in list1:
    print("letter is vowel")
else:
    print("letter is not vowel ")'''

# if two value  same sum will be zero 
'''a=int(input("enter number a"))
b=int(input("enter number b"))
c=int(input("enter number c"))

if a==b or b==c or c==a:
     a=a+b+c
     print(a)
   
else:
    print(0)'''

# differnce 5 return true 
'''n=int(input("enter n "))
n1=int(input("enter n1 "))

if n-n1==5 or n==n1 or n+n1:
    print (True)
else:
   print(False)'''

# sum of positive number 
'''n=int(input("n positive number "))
sum=0
for i in range(n):
    sum=sum+i
print(sum)'''

# len of string 

'''string=("hii km che ")
count=0
for i in string:
    count+=1
print(count)


print(len(string))

   '''
# character frequency 

'''string=("helloo km che ")
s={}

for i in string:
    if i in s: 
     s[i]=s[i]+1
    else:
       s[i]=1
print(s)
'''

# swap first two character 

'''x=("hi km che ")
y=("no i am ")

a=x[:2]+y[2:]
b=y[:2]+x[2:]
print(a)
print(b)
'''


'''s1=(input("enter string "))


if len(s1)>=3 and s1.endswith('ing'):
    print('stringly')
elif len(s1)<3:
    print(s1)
else:
    print(s1+'ing')

'''

# insert middle


'''string=input("enter string ")
print(string )
mid=input("what you can add in the middle of the string ")
temp=string.split()
pos=len(temp)//2
res=(temp[:pos]+[mid]+temp[pos:])
print(' '.join(res))'''


# first 2 and last 2
'''string=input("enter string ")
 
if  len(string)<2:
  print()
else:
 print(string[:2]+string[-2:])'''

# string multilpe of 4 
'''
string=input("enter string ")

if len(string)%4==0:
    print(string[::-1])
else:
    print(string)
'''
# find the longest one

'''n=input("enter string")
longest=0

for i in n.split():
    if len(i)>longest:
        longest=len(i)
print(len(i),i)

'''

##################################  assignment 2  ################################## 


#sum and large and small
'''
l1=[5,6,7,2]
sum=0
for i in l1:
    sum=sum+i
print(sum)
   '''

#largest or smallest
'''l1=[5,6,7,2]
largest=l1[0]
small=l1[0]

for i in l1:
    if i>largest:
        largest=i
    elif i<small:
        small=i

print(small)
print(largest)

'''
# len les 2 
'''list=['yogi','rinr','malayalam']
count=0
for i in list:
   if len(i)>=2 and i[0]==i[-1]:
      count+=1
print(count)
      '''

# remove duplicates from list
'''list1=[1,2,3,2,1]
print(list(set(list1)))
'''
# empty list
'''
list=[]

if list==[]:
    print("yess")
else:
    print("no")
'''
# common member return trure 
'''def common_member(list1, list2):
    return bool(set(list1).intersection(list2))
list1=[1,2,3]
list2=[2,5,6]
print(common_member(list1,list2))'''


# first and last element 
'''li=[]

for i in range(1,30):
    li.append(i**2)
print(li[:5])
print(li[-5:])
'''
# list of character into list
'''list=['y','o','g','i']
print(''.join(list))
'''

# select item randlomyly

'''list=[1,2,3,4,5,6]
import random
pi=random.choice(list)
print(pi)'''


# second smallest number

'''li1=[1,2,3,4,5]
list.sort(li1)
print(li1[-2])
'''

# tuple with number
'''tuple=(1,2,3)
print(tuple)'''

# tuple with differnt 
'''
tup=(1,2,'yogi','rue')
print(tup)'''


# list into variable
'''list=[(1,2,3),(8,9,6,4),(5,4,3)]
s1,s2,s3=list
print(s1)
print(s2)
print(s3)'''

# len of tuple

'''tuple1=(1,2,3,4)
print(len(tuple1))'''

# list into tuple 
'''
list=[1,2,3]
print(tuple(list))'''

# revese a tuple
'''tup=(2,3,4)
print(tup[::-1])'''

# tuple into string
'''
tup=('y','o','g','i')
print(''.join(tup))'''

# tup is exit 
'''tup=(1,2,3,4)
if 1 in tup:
    print("yes")
else:
    print("noo")'''


# list of tuple add new vale 

'''def replace_last_value(tuples_list, new_value):
    return [t[:-1] + (new_value,) for t in tuples_list]

tuples_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value = 100
print(replace_last_value(tuples_list, new_value))
'''

# repeated item 

'''tup=(1,3,4,2,1,4,8)

for i in tup:
    if tup.count(i)>1:
        print(i)'''

#list of tuple remove empty
'''l=[1,2,3,(),6,(),()]

for i in l:
    if i!=():
        print(i)
'''
# unzip 

'''def unzip_list_of_tuples(list_of_tuples):
    return list(map(list, zip(*list_of_tuples)))


list_of_tuples = [(1, 2), (3, 4), (8, 9)]
unzipped_lists = unzip_list_of_tuples(list_of_tuples)
print(f"The unzipped lists are {unzipped_lists}")'''


# tuple into dict 
'''def convert_to_dict(tuples):
    result = {}
    for key, value in tuples:
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
    return result

tuples = [('apple', 1), ('banana', 2), ('apple', 3), ('banana', 4), ('orange', 5)]
dictionary = convert_to_dict(tuples)
print(dictionary)
'''
# uniq in dict 
'''
d = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
print(list(set(d.values())))'''


# merge two python dict 
'''d1={'name':'yogi','age':21,'city':'rajkot'}
d2={'roll':2,'state':'gujrat'}

d1.update(d2)
print(d1)'''

# two list in one dict

'''key=['name','age','city']
value=['yogi',20,'rajkot']
dict={}
for i in key:
    for j in value:
        dict[i]=j
        value.remove(j)
        break
print(dict)
'''

# multiple key exit in dict
'''d={1:'yogi',2:'rinku',3:'krishna',4:'nayna'}
print(d)
if 1 in d:
    print("yess")
else:
    print("noo")
'''


'''def check_keys_exist(d, keys):
    return all(key in d for key in keys)

my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
keys_to_check = ['name', 'state']
if check_keys_exist(my_dict, keys_to_check):
    print(f"All keys {keys_to_check} exist in the dictionary.")
else:
    print(f"At least one key from {keys_to_check} is not present in the dictionary.")

'''

# dict with number 

'''dict1={}
for i in range(1,15):
    dict1[i]=i
print(dict1)
'''

# cheak key present or not 
'''my_dict = {"name": "Alice", "age": 25, "city": "New York"}
key = "age"

if key in my_dict:
    print(f"{key} is present in the dictionary.")
else:
    print(f"{key} is not present in the dictionary.")
'''

'''
statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}

keys = statesAndCapitals.keys()
print(keys)'''

#dict merge dict

'''d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {**d1, **d2}
print (d3)
'''
#dict into tuple 
'''
data = { ("chapathi", "roti"): 'Bobby', ("Paraota", "Idly", "Dosa"): 'ojaswi'}
print(tuple(data))'''


# listof tuple into dict
'''tup=('apple', 1), ('banana', 2), ('gavava', 3)
print(dict(tup))'''



# same key no pluse in dict 
'''d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

for key in d2:
    if key in d1:
        d2[key] += d1[key]
    else:
        pass

d3 = {**d1, **d2}

print("The combined dictionary is: ", d3)
'''                         


# each letter

'''data={'1': ['a','b'], '2': ['c','d']}

for x in data['1']:
    for y in data['2']:
        print(x + y,end=" ")
    '''


# highest 3 value 
'''my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}
result = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:3])
print(result)'''



'''def dict(string):
  dict={}
  for char in string:
    if char in dict:
      dict[char]+=1
    else:
      dict[char]=1
  return dict
print(dict('w3resource'))
'''

# fact
'''n=int(input("enter n"))
fact=1
for i in range(n,1,-1):
    fact=fact*i
print(fact)
'''

# num is present or not 
'''n=int(input("enter number"))

for i in range(1,20):
    if i==n:
        print("yes")
        break
'''

# string palindrom or not 
'''string=input("enter string")
st=string[::-1]

if string==st:
    print("yes")
else:
    print("noo")
'''

# perfact or not
'''
n=int(input("enter number "))
x=n
sum=0

for i in range(1,n):
   if n%i==0:
      sum=sum+i

if x==sum:
   print("yess")
else:
   print("noo")'''


# random number 

'''import random
print(random.random())'''

 #random form tuple
'''import random
list=[1,2,3,4,]
print(random.choice(list))'''

# random from range

'''import random
print(random.randrange(1,20))
'''

'''import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)

print(f"The shuffled list is: {my_list}")'''



'''from decimal import Decimal

data = list(map(Decimal, '2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
print(f"The maximum number is {max(data)} and the minimum number is {min(data)}.")
'''
# sum  of divisor
'''
divisor=[1]
n=int(input("enter number "))
for i in range(2,n):
    if n%i==0:
        divisor.append(i)
print(sum(divisor))
'''

# areaa of peralellogram
'''
base=float(input("enter float"))
height=float(input("enter rheight"))

area=base*height
print(area)
'''

# area of trapizoid
'''height = float(input("Height of trapezoid: "))
base_1 = float(input('Base one value: '))
base_2 = float(input('Base two value: '))
area = ((base_1 + base_2) / 2) * height
print("Area is:", area)
'''

'''n=float(input("ener radian"))
pi=3.14
degree=n*(180/pi)
print("degree is ",degree)'''


# list comphension


'''l1=[i for i in range(1,10) if i%2==0]
print(l1)
'''

# dict comphension

'''d1={i: f"item{i}"for i in range(1,10)}
d2={value:key for key,value in d1.items()}
print(d2,"\n",d1)'''

# set comphension

'''n={i for i in [1,2,3,1,1,1]}
print(type(n))
print(n)
'''

# Genretor
'''
evens=(i for i in range(1,100) if i%2==0)
print(type(evens))
print(evens.__next__())
print(evens.__next__())'''

# area of cylinder and volume of 
'''
pi=3.14
radius=float(input("plase enter the radius of the cylinder:"))
height=float(input("plase enter the height of the cylinder "))

area=2*pi*radius*(radius+height)
volume=pi*radius*radius*height
print(area)
print(volume)'''


# dict with common value 
'''data=[{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
com={}
for  d in data:
    item=d['item']
    amount=d['amount']
    if item in com:
        com[item]+=amount
    else:
        com[item]=amount
print(com)
  '''

# Define a lambda function that takes one argument (x) and returns its square
'''x=lambda x:x**2
print(x(5))'''


# number is perfact or not 
'''num = int(input("Please enter a number: "))
sum = 0

for i in range(1, num):
    
    if num % i == 0:
        sum += i

if sum == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")
'''

# zip funcation
'''a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(tuple(x))
'''

# armstrong number
'''num = int(input("Enter a number: "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** len(str(num))
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
'''

# perfect number 
'''
n=int(input("enter number "))
sum=0
temp=n


for i in range(1,n):
    if n%i==0:
        sum+=i

if n==sum:
    print("yess")
else:
    print("noo")
'''

#palindom 
'''
n=int(input("enter number"))
rev=0
temp=n


while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp//=10

if n==rev:
    print("yess")
else:
    print("nooo")
'''


# remove duplicate from list 
'''
list1=[1,2,3,4,3,2,14,4,7]
l1=[]

for i in list1:
    if i not in  l1:
        l1.append(i)
print(l1)
  
'''

# factorial number
'''
num=int(input("enter number"))
fact=1


if num<0:
    print("factorial number doent exit of negative number ")
elif num==0:
    print("factorial numbeer of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("fact number is ",fact )

'''

# fibboo

'''n=int(input("enter number"))

a=1
b=1
print(a)
print(b)
for i in range(2,n+1):
    c=a+b
    a=b
    b=c
    print(c)'''


# list comphersion''
'''
l=[1,2,3,4,5,6,7,8,9]

new=[i for i in l if i%2==0]
print(new)'''

# creating an array with integer type
'''import array as arr
a = arr.array('i', [1, 2, 3])
print(type(a))
for i in a:
    print(i, end=" ")'''


#  dict comphensiion
'''
dict1={504:'apple',102:'banana',123:'cherry'}
d2= {k: v for k,v in sorted (dict1.items(),key=lambda x:x[1])}
print(d2)'''


# sort and sorted
'''l=[6,7,8,4,3]
l.sort()
n=sorted(l)
print(n)
print(l)'''



# is or == operator
'''list1 = []
list2 = []
list3 = list1

if (list1 == list2):
 print("True")
else:
 print("False")


if (list1 is list3):
    print("True")
else:
    print("False")'''


