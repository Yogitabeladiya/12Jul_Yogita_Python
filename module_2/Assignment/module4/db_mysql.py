
import pymysql

'''try:
    con=pymysql.connect(host='localhost',user='root',password='',database='test1.db')
    print("connected....!")
except Exception as e:
    print(e)

cr=con.cursor()'''
'''create="create table y2(id integer primary key auto_increment ,name text,city text)"
try:
    cr.execute(create)
    print("Table created")
except Exception as e:
    print(e)


'''
# insert 
'''insert="insert into y2 (name,city) values('yogita','rajkot'),('rinkal','atk')"
try:
    cr.execute(insert)
    con.commit()
    print("record inserted")
except Exception as e:
    print(e)'''

# update 
'''update="update y2 set name='yogi' where id=1"
try:
    cr.execute(update)
    con.commit()
    print("update record")
except Exception as e:
    print(e)'''

'''delete="delete from y2 where id=2"
try:
    cr.execute(delete)
    con.commit()
    print("delete record sucessfully")
except Exception as e:
    print(e)'''

# select
'''select="select * from y2"
try:
  cr.execute(select)
  selct=cr.fetchall()
  for i in selct:
   print(i)'''
'''select=cr.fetchone()
  print(select)
'''
'''select=cr.fetchone()
  print(select)
'''
'''except Exception as e:
   print(e)
'''



'''tn=input("table name ")
table1=int(input("How many column you want "))
try:
    l=[]
    for i in range(table1):
       l.append(input(f"enter column{i} and datatype:"))
       column=" ,".join(l)
    con.execute(f"create table {tn} ({column})")
    print("Table cerated")
except Exception as e:
    print(e)'''


import pymysql
try:
    con=pymysql.connect(host='localhost',user='root',password='',database='test1.db')    
    print("connected")
except Exception as e:
    print(e)

cr=con.cursor()
table_name=input("Enter table name")
colum=int(input("How many column you want "))

for i in range(colum):
        nm=input("enter name ")
        sub=input("enter sub")
        try:
           cr.execute(f"create table{table_name}({nm})({colum})")
           con.commit()
           print("inserted...")
        except Exception as e:
               print(e)

