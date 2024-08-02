from tkinter import *

def fun1(event):
    w.config(bg='white')
    l1.config(text=event.x)
    l2.config(text=event.y)

w=Tk()
w.geometry("400x500+30+40")

l1=Label(w)
l2=Label(w)
l1.pack()
l2.pack()

w.bind("<Motion>",fun1)
