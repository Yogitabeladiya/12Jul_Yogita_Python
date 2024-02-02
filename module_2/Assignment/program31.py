# multiple keys in exist or not


def cheak(dict,keys):
    return all(keys in dict)
my_dict={'name':'yogi','age':12,'city':'rjk'}
keys_to=['name','age']

if cheak(my_dict,keys_to):
    print("present")
else:
    print("not present")


