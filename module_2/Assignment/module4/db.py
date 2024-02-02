'''import sqlite3

try:
    con=sqlite3.connect('testdb.db')
    print("Database crated")
except Exception as e:
    print(e)'''


import sqlite3
# database cretaed
try:
    con=sqlite3.connect('test.db')
    print("Database cerated")
except Exception as e:
    print(e)
'''
# table cerated
tn=input("table name ")
table1=int(input("How many column you want "))
try:
    l=[]
    for i in range(table1):
       l.append(input(f"enter column{i} and datatype:"))
       column=" ,".join(l)
    con.execute(f"create table {tn} ({column})")
    print("Table cerated")
except Exception as e:
    print(e)
'''

'''insert="insert into y1 (id,name) values(4,'yogi'),(5,'bubali'),(6,'tamli')"
try:
    con.execute(insert)
    con.commit()
    print("record inserted")
except  Exception as e:
    print(e)
'''

'''update="update y1 set name='yogit' where id=3"
try:
    con.execute(update)
    con.commit()
    print("record updated sucessfully ")
except Exception as e:
    print(e)
'''

'''delete="delete from y1 where id=3"
try:
    con.execute(delete)
    con.commit()
    print("delete record from table sucessfully")
except  Exception as e:
    print(e)'''

cr=con.cursor()
select="select * from y1"
try:
    
    cr.execute(select)
    select=cr.fetchall()
    for i in select:
        print(i)
except Exception as e:
    print(e)



# insertdata
'''insert="insert into student1(name,city)
try:
    con.execute(insert)
    con.commit()
    print("Record inserted")

except Exception as e:
    print(e)'''