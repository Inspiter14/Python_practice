from tkinter import *

def sub():
    a=int(e1.get())
    b=int(e2.get())
    c=a-b
    l1.config(text=c,bg="blue",fg="white")

def add():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b
    l1.config(text=c,bg="blue",fg="white")

def mul():
    a=int(e1.get())
    b=int(e2.get())
    c=a*b
    l1.config(text=c,bg="blue",fg="white")

def div():
    a=int(e1.get())
    b=int(e2.get())
    c=a/b
    l1.config(text=c,bg="blue",fg="white")
    
    
w1=Tk()
w1.geometry("500x550+30+30")

e1=Entry(w1)
e1.place(x=180,y=50)
e2=Entry(w1)
e2.place(x=180,y=110)

l1=Label(w1)
l1.place(x=180,y=150)

radio=IntVar()
r1=Radiobutton(w1,text="Sub",variable=radio,value=1,command=sub).place(x=40,y=230)
r2=Radiobutton(w1,text="Add",variable=radio,value=2,command=add).place(x=100,y=230)
r3=Radiobutton(w1,text="Mul",variable=radio,value=3,command=mul).place(x=160,y=230)
r4=Radiobutton(w1,text="Div",variable=radio,value=4,command=div).place(x=220,y=230)

