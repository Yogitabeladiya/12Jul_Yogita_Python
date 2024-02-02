'''dict={'id':1,'name':'yogita','city':'rajkot'}

print(dict)
print(dict['id'])
print(dict['name'])
print(dict.get('name'))
print(len(dict))
print(dict.keys())
print(dict.values())
dict.pop('id')
del dict['name']
dict['id']=2
dict['city']='rajkot'
dict.clear()
print(dict)

ndict=dict.copy()
print(ndict)
'''
'''if 'name' in dict:
    print("yes ...")
else:
    print("nooo")

'''

'''for i in dict:
    print(i)

for i in dict.values():
    print(i)

for i in dict.items():
   print(i)

if 'yogita' in dict.values():
    print("yes")
else:
    print("nooo")

if 'id' in dict.keys():
    print("ys")
else:
    print("noo")'''



d={1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(d)


'''str="this is python python is powerfull"
l1=[]

for i in str.split():
    if i not in l1:
        l1.append(i)
print(" ".join(l1))
    '''

'''str="my name is yogita"
a=str.split()
a.pop()[:2]
print(a)'''



'''x=[[1,2,3],
    [4,5,6],
    [7 ,8,9]]
 
y= [[9,8,7],
    [6,5,4],
    [3,2,1]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]
        ]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]
for r in result:
    print(r)


'''

my_list = [i for i in range(1, 10)]
print(i)