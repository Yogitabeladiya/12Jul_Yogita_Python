'''Write a Python program to combine two dictionary adding values for 
common keys.''' 


'''dict1 = {'a': 100, 'b': 200, 'c':300} 
dict2 = {'a': 300, 'b': 200,'d':400} 
dict={}

c = {i: dict1.get(i, 0) + dict2.get(i, 0)

     for i in set(dict1).union(dict2)}
    

print(dict(c))




for i in dict1.items():
    if i in dict2.items():
        dict[i]
    else:
        dict[i]
print(dict)

''' 

# dict 
'''
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d = {k: d1.get(k,0) + d2.get(k,0) for k in d1.keys() | d2.keys()}
print(d)'''