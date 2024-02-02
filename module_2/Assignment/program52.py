

'''data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
combined = {}

for d in data:
    item = d['item']
    amount = d['amount']
    if item in combined:
        combined[item] += amount

    else:
        combined[item] = amount


print(combined)
'''
data=[{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
com={}

for  d in data:
    item=d['item']
    amount=d['amount']
    if item in com:
        com[item]+=amount
    else:
        com[item]=amount
print(com)
  