#Write a Python program to find the maximum and minimum numbers 
# the specified decimal numbers.


from decimal import decimal 

'''data = list(map(Decimal, '2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
print("Maximum: ", max(data))
print("Minimum: ", min(data))


'''

data=list('2.34 2.45 3.45 2.oo'.split())
print("maximum",max(data))
print("Minimum",min(data))