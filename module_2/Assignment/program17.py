# reverse tuple


'''t1=(4,5,6,7,8)
print(t1[::-1])
'''

'''my_dict={'orange':'fruit', 'potato':'vegetables', 'banana':'fruit' 
}
output={}
for ele in rangemy_dict():
    print(ele)
    if my_dict[ele] not in output:
        output[my_dict[ele]]=ele
    else:
        output[my_dict[ele]].append(ele)
print(output)
'''


'''my_dict = {"a": 1, "b": 2, "c": 3, "d": 2, "e": 4, "f": 1}
unique_values = set()
for value in my_dict.values():
    unique_values.add(value)
print("The unique values in the dictionary are:",unique_values)
for value in unique_values:
    print(value)
print("The number of unique values is:", len(unique_values))
'''
# factrial number using recursion 
'''def factorial(n):
  if n==0 or n==1:
     return 1
  else:
     return n*(factorial(n-1))
print(factorial(5))
print(factorial(4))
'''


# fibbonacci series
'''def fibonacci(n):
    if n <= 0:
        return "Incorrect input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 10
for i in range(1, n):
    print(fibonacci(i), end=" ")
'''


# fibonacci series
'''a,b=0,1
n=int(input("enter number"))
if n==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,n):
       c=a+b  
       a=b   
       b=c   
       print(c)  
'''



# factorial number 
'''n=int(input("Enter number"))
fact=1
for i in range(n,1,-1):
    fact *= i
print(fact)
'''

