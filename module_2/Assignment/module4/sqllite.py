import sqlite3
try:
    con=sqlite3.connect('test1db.db')
    print("connected")
except Exception as e:
    print(e)

# create table

'''try: 
 crate="create table studentinfo (id integer primary key autoincrement , name text, sub text)"
 con.execute(crate)
 print("table created")
except Exception as e:
   print(e)'''

# insert record

'''try:
    insert="insert into studentinfo (name , sub) values('yogita','python'),('tamli','python'),('babali','python'),('yogi','python'),('gita','python')"
    con.execute(insert)
    con.commit()
    print("record inserted")
except Exception as e:
    print(e)'''



'''try:
    update="update studentinfo set name='gitudi' where id=2"
    con.execute(update)
    con.commit()
    print("update sucessfully")
except Exception as e:
    print(e)'''


'''try:
    delete ="delete from studentinfo where id=2"
    con.execute(delete)
    con.commit()
    print("deleted sucessfully")

except Exception as e:
    print(e)'''



cr=con.cursor()
data="select * from studentinfo"
try:
    cr.execute(data)
    '''data=cr.fetchall()
    for i in data:
      print(i)'''
    '''data=cr.fetchone()
    print(data)'''
    data=cr.fetchmany(3)
    for i in data:
        print(i[2])
except Exception as e:
    print(e)