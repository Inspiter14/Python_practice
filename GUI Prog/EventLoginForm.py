from tkinter import *
from tkinter import messagebox  #to show dailog box with perticular message

def submit():
    if len(e1.get())!=0 and len(e2.get())!=0:
        messagebox.showinfo("Message","Form Sumbitted !")
    else :
        messagebox.showinfo("Warning","Please Enter Username and Password !")


def reset():
    e1.delete(0,"end") #delete fun is used to erase everything
    e2.delete(0,"end")

w1=Tk()
w1.config(bg='white')
w1.geometry("320x250+20+30")
w1.title("Login Form")

l1=Label(w1,text="Username :")
l2=Label(w1,text="Password :")

e1=Entry(w1,width='20')
e2=Entry(w1,show='#')  #show is the attribute to decide what will it shows when we type in Entry widget

b1=Button(w1,text="Sumbit",command=submit) #command is use to handle the event
b2=Button(w1,text="Reset",command=reset)

l1.place(x=80,y=40)
l2.place(x=80,y=70)

e1.place(x=170,y=40)
e2.place(x=170,y=70)

b1.place(x=80,y=120)
b2.place(x=170,y=120)
