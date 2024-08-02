from tkinter import *

w=Tk() #creating a window
w.title('Login Form')
w.geometry('800x700')
w.config(bg="white")

#Creating Labels:
l1=Label(w,text="Name :")
l2=Label(w,text="Collage Name :")
l3=Label(w,text="Address :")
l4=Label(w,text="Gendre :")
l5=Label(w,text="Department :")
l6=Label(w,text="Interest Areas :")
l7=Label(w,text="Qualification")

l1.grid(row=1,column=2,sticky="N")
l2.grid(row=2,column=2)
l3.grid(row=3,column=2)
l4.grid(row=4,column=2)
l5.grid(row=5,column=2)
l6.grid(row=6,column=2)
l7.grid(row=7,column=2)

#Creating Entry to take single-line i/p:
e1=Entry(w).grid(row=1,column=4)
e2=Entry(w).grid(row=2,column=5)

#Creating Text to take multi-line i/p:
t1=Text(w,width=30,height=2).grid(row=3,column=5)

#Creating RadioButton:
radio1=IntVar()
radio2=IntVar()
r1=Radiobutton(w,text="Male",variable=radio1,value=1).grid(row=4,column=4)
r2=Radiobutton(w,text="Female",variable=radio1,value=2).grid(row=4,column=5)
r3=Radiobutton(w,text="Computer",variable=radio2,value=1).grid(row=5,column=4)
r4=Radiobutton(w,text="IT",variable=radio2,value=2).grid(row=5,column=5)

#Creating ChechButton:
check=IntVar()
c1=Checkbutton(w,text="AI",onvalue=1,variable=check).grid(row=6,column=4)
c2=Checkbutton(w,text="CYBER",onvalue=1,variable=check).grid(row=6,column=5)
c3=Checkbutton(w,text="ML",onvalue=1,variable=check).grid(row=6,column=6)
c4=Checkbutton(w,text="DATA SCIENCE",onvalue=1,variable=check).grid(row=6,column=7)

#Creating List:
l1=Listbox(w)
l1.insert(1,"10th")
l1.insert(2,"12th")
l1.grid(row=8,column=4)
