from tkinter import *
from tkinter import messagebox  #to show dailog box with perticular message
import mysql.connector as ms

def submit(eve):
    con=ms.connect(host="localhost",database="emp",username="root",password="123456") #create connection object
    cur=con.cursor() #create cursor object
    a=e1.get()
    q1="select * from employee where id='"+a+"' " #write your query
    cur.execute(q1)
    data=cur.fetchone()
    i2.set(data[1])
    i3.set(data[2])
    i4.set(data[3])    

def resest():
    e1.delete(0,"end")
    e2.delete(0,"end")
    e3.delete(0,"end")
    e4.delete(0,"end")

w1=Tk()
w1.config(bg='white')
w1.geometry("420x350+550+240")
w1.title("Login Form")

l1=Label(w1,text="ID :")
l2=Label(w1,text="Name :")
l3=Label(w1,text="Post :")
l4=Label(w1,text="Salary :")

i2=StringVar()
i3=StringVar()
i4=IntVar()

e1=Entry(w1)
e2=Entry(w1,textvariable=i2)  
e3=Entry(w1,textvariable=i3)
e4=Entry(w1,textvariable=i4)

b1=Button(w1,text="Fetch") #command is use to handle the event
b2=Button(w1,text="Reset",command=resest)

b1.bind("<Return>",submit)
b1.bind("<Button>",submit)
l1.place(x=80,y=40)
l2.place(x=80,y=70)
l3.place(x=80,y=100)
l4.place(x=80,y=130)

e1.place(x=170,y=40)
e2.place(x=170,y=70)
e3.place(x=170,y=100)
e4.place(x=170,y=130)

b1.place(x=100,y=200)
b2.place(x=170,y=200)

