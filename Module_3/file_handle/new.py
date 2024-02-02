
import sqlite3
try:
    con=sqlite3.connect("testdb.db")
    print("connected....")
except Exception as e:
    print(e)

tbl=input("enter table name:")
row=int(input("enter how many row to want you:"))
for i in range(row):
    filed=input("enter column name: and its type ")
    x=f"create table {tbl}({filed})"

try:
    con.execute(x)
    print("table created....")

except Exception as e:
    print(e)