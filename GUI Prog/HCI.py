from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_dosa.delete(0,END)
    entry_tea.delete(0,END)

def Total():
    try:a1=int(dosa.get())
    except:a1=0

    try:a2=int(tea.get())
    except:a2=0

    c1=a1*60
    c2=a2*10

    total_bill=Label(f3,font=("aria",20,"bold"),text="Total",width=18,fg="lightyellow",bg="black")
    total_bill.place(x=0,y=84)

    cost=c1+c2
    string_cost="Rs."+ str(cost)
    Total_cost.set(string_cost)

    entry_total=Entry(f3,font=("aria",20,"bold"),textvariable=Total_cost,bd=6,width=12)
    entry_total.place(x=60,y=140)

Label(text="Bill Management",bg="black",fg="white",font=("calibri",33),width=50,height=2).pack()

#Menu Card  Frame 1
f1=Frame(root,bg="lightgreen",width=300,height=370)
f1.place(x=10,y=122)

Label(f1,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)
Label(f1,text="Dosa...Rs.60/plate",font=("Lucida Calligraphy",15,"bold"),fg="black",bg="lightgreen").place(x=10,y=90)
Label(f1,text="Tea...Rs.10/plate",font=("Lucida Calligraphy",15,"bold"),fg="black",bg="lightgreen").place(x=10,y=120)

#Bill  Frame 3
f3=Frame(root,height=370,width=300,bg="lightyellow")
f3.place(x=690,y=122)

Bill=Label(f3,text="Bill",bg="lightyellow",font=("calibri",30))
Bill.place(x=120,y=20)

#Entry Work   Frame 2
f2=Frame(root,height=380,width=300,bd=5,relief=RAISED)
f2.pack()

dosa=StringVar()
tea=StringVar()
Total_cost=StringVar()

lb_dosa=Label(f2,font=("aria",20,"bold"),text="Dosa",width=10,fg="blue4")
lb_tea=Label(f2,font=("aria",20,"bold"),text="Tea",width=10,fg="blue4")

lb_dosa.grid(row=1,column=0)
lb_tea.grid(row=2,column=0)

entry_dosa=Entry(f2,font=("aria",20,"bold"),textvariable=dosa,bd=6,width=10,bg="lightpink")
entry_tea=Entry(f2,font=("aria",20,"bold"),textvariable=tea,bd=6,width=10,bg="lightpink")

entry_dosa.grid(row=1,column=1)
entry_tea.grid(row=2,column=1)

reset_btn=Button(f2,fg="black",bg="lightblue",font=("aria",16),width=12,text="Reset",command=Reset)
total_btn=Button(f2,fg="black",bg="lightblue",font=("aria",16),width=12,text="Total",command=Total)

reset_btn.grid(row=3,column=0)
total_btn.grid(row=3,column=1)

root.mainloop()

