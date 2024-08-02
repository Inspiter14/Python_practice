from tkinter import *

'''
to get the input written in Text widget we need to pass 2 args:
1. Starting index i.e from which index we want to get
2. Ending index i.e upto which point want to get
to perform the functions like insert(), delete(), get(),etc. where we perform operations on i/p of Text widget we need to pass
the these parameters as args.
For e.g, delete(1.0,"end-1c") where 1.0 describes that start from 1st index and end-1c describes that delete upto last
'''
def check():
    cnt=0
    str1=t1.get(1.0,"end-1c")
    #print(str1.find(' '))
    for i in str1:
        if i==' ' or i=='.':
            cnt=cnt+1
    length=len(t1.get(1.0,"end-1c"))
    actlen=length-cnt
    #print(actlen)    
    if actlen>60:    
        t1.delete(1.0,"end-1c")
        l4.config(text="Length is greather than 60 chars !",fg="blue",bg="white")
    elif actlen==0:
        l4.config(text="Please write in the Comment Section first !",fg="blue",bg="white")
    else:
        #print(len(t1.get(1.0,"end-1c")))
        l4.config(text="Length is less than 60 chars !",fg="blue",bg="white")
        
w1=Tk()
w1.config(bg='white')
w1.geometry("500x300+280+190")
w1.title("Check Comment Length")

l1=Label(w1,text="Check whether the comment has 60 characters or not")
l2=Label(w1,text="Username :")
l3=Label(w1,text="Comment :")
l4=Label(w1)

l1.place(x=110,y=40)
l2.place(x=110,y=80)
l3.place(x=110,y=120)
l4.place(x=145,y=250)

e1=Entry(w1)
e1.place(x=200,y=80)

t1=Text(w1,width=30,height=4)
t1.place(x=200,y=120)

b1=Button(w1,text="Check",command=check)
b1.place(x=220,y=220)

