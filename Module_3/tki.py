from tkinter import*
from tkinter import messagebox as mb

def add():
    x=int(e.get())+int(e1.get())
    mb.showinfo("addtion",f"addtion is {x}")

def sub():
    x=int(e.get())-int(e1.get())
    mb.showinfo("subtraction",f"subtraction is {x}")

def mul():
    x=int(e.get())*int(e1.get())
    mb.showinfo("multiplication",f"multiplication is {x}")

def div():
    x=int(e.get())/int(e1.get())
    mb.showinfo("division",f"division is {x}")


top=Tk()
top.title("calculator")
top.config(background="yellow")
top.geometry("500x400")
l=Label(top,text="enter a",font=30,bg="yellow")
l.grid(row=0,column=0)
e=Entry(top,font=30,bg="yellow")
e.grid(row=0,column=1)

l=Label(top,text="enter b",font=30,bg="yellow")
l.grid(row=1,column=0)
e1=Entry(top,font=30,bg="yellow")
e1.grid(row=1,column=1)

b=Button(top,text="add",font=30,command=add,bg="yellow",activebackground="green")
b.place(x=20,y=60)


b1=Button(top,text="sub",font=30,command=sub,bg="yellow",activebackground="green")
b1.place(x=80,y=60)


b2=Button(top,text="mul",font=30,command=mul,bg="yellow",activebackground="green")
b2.place(x=140,y=60)

b3=Button(top,text="div",font=30,command=div,bg="yellow",activebackground="green")
b3.place(x=200,y=60)



top.mainloop()