from tkinter import *

def fun(evt):
    obj=evt.widget  #we can get the info that which button is clicked by using evt.widget
    w1.config(bg=obj.cget('bg'))
    #cget fun is used to get the configuration info of a widget for e.g here we use 'bg' we can also use 'fg'
    #it reduces code

w1=Tk()
w1.geometry("300x200+40+120")

b1=Button(text="Blue",bg="blue")
b2=Button(text="Yellow",bg="yellow")

b1.bind("<Button>",fun)
b2.bind("<Button>",fun)

b1.pack()
b2.pack()
