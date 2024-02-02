import datetime

x=datetime.datetime.now()
print(x)
print("day",x.day)
print("month",x.month)
print("year",x.year)


print("hour",x.hour)
print("minute",x.minute)
print("second",x.second)
print("microsecond",x.microsecond)

'''import random
captcha=['jgec','luy53','uyt21','fdre2','juy4']
x=random.choice(captcha)
print(x)
print(captcha)
random.shuffle(captcha)
print(captcha)'''

import random
x=random.random()
x=random.randint(1111,9999)
print(x)
print(random.randrange(1111,4444,130))
