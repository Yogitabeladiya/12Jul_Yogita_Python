import re

mystr="This is python!"
#x=re.findall('^This',mystr)
#x=re.findall('^[A-Z]',mystr)
#x=re.findall('[^A-Z]',mystr)
#x=re.findall('on!',mystr)
x=re.findall('on$',mystr)
print(x)