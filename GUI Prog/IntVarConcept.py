from tkinter import *

'''we need to pass 1 arg to fun in which we are handling our event, caz that object stores
the related data about perticular event that we are going to handle '''

def fun1(event): 
    a=e1.get()
    b=e2.get()
    c=int(a)+int(b)
    if a!=0:
        v1.set(c)
        
      #c=int(a)+int(b)
    #v1.set(c)  #we can set the value using set(), but only can use a "variable" which can be defined to set values

w=Tk()
w.geometry("400x500+30+50")

v1=IntVar() #we can define IntVar(),StringVar(),FloatVar()

e1=Entry(w)
e2=Entry(w)
e3=Entry(w,textvariable=v1) #we need to pass that IntVar() variable to that widget whose value we want to set 

e1.pack()
e2.pack()
e3.pack()

e1.bind("<Return>",fun1) #
e2.bind("<Return>",fun1)
e3.bind("<Return>",fun1)
