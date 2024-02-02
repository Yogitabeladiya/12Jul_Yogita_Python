import re

#n=int(input("enter string "))
n="yogita23455This is mme"
#x=re.findall('[A-Z]',n)
#x=re.findall('[a-z]',n)
#x=re.findall('[A-za-z]',n)
#x=re.findall('[0-9]')
x=re.findall('[A-Za-z0-9]',n)
print(x)