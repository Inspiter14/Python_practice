from tkinter import *
from tkinter import messagebox  #to show dailog box with perticular message
import mysql.connector as ms

def submit():
    con=ms.connect(host="localhost",database="sample",username="root",password="123456") #create connection object
    c1=con.cursor() #create cursor object
    q1="insert into register values(%s,%s,%s)" #write your query
    
    if len(e1.get())!=0 and len(e2.get())!=0 and len(e3.get())==10:
        val=(e1.get(),e2.get(),e3.get()) #get the values which you want to insert and make a tuple of them
        c1.execute(q1,val) #execute the query
        con.commit() #commit it
        messagebox.showinfo("Save Message","Record Stored Successfully !")
        con.close() #close the connection

    else:
        messagebox.showinfo("Warning","Please fill all the feilds carefully !")

def resest():
    e1.delete(0,"end")
    e2.delete(0,"end")
    e3.delete(0,"end")

w1=Tk()
w1.config(bg='white')
w1.geometry("320x250+550+240")
w1.title("Login Form")

l1=Label(w1,text="User Name :")
l2=Label(w1,text="Password :")
l3=Label(w1,text="Mob Number :")

e1=Entry(w1,width='20')
e2=Entry(w1,show='*')  #show is the attribute to decide what will it shows when we type in Entry widget
e3=Entry(w1)

b1=Button(w1,text="Sumbit",command=submit) #command is use to handle the event
b2=Button(w1,text="Reset",command=resest)
l1.place(x=80,y=40)
l2.place(x=80,y=70)
l3.place(x=80,y=100)


e1.place(x=170,y=40)
e2.place(x=170,y=70)
e3.place(x=170,y=100)

b1.place(x=80,y=150)
b2.place(x=170,y=150)

