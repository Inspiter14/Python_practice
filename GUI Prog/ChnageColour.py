from tkinter import *

def colour1():
    w1.config(bg="red")

def colour2():
    w1.config(bg="blue")

def colour3(event):
    w1.config(bg="white")    

w1=Tk()
w1.geometry("500x300+60+80")
w1.title("Change Colour")
w1.config(bg='white')

l1=Label(w1,text="Tap on Button to change the Window's Colour")
l1.place(x=120,y=70)

b1=Button(w1,text="Red",command=colour1)
b2=Button(w1,text="Blue",command=colour2)

b1.place(x=150,y=120)
b2.place(x=280,y=120)

w1.bind("<Button>",colour3)
