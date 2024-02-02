
# divisor 
'''def sum_div(number):
    divisor=[1]
    for i in range(2,number):
        if (number%i)==0:
            divisor.append(i)
    return sum(divisor)
print(sum_div(8))
'''


d={'abc':74,'xyz':65,'pqr':88,'efg':89}
a=sorted(d.items(), key=lambda x:x[0])  
print(dict(a))