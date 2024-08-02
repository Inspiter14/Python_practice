from tkinter import *

'''
How to create List of Objects: E.g Button:
1.Create an empty list
2.Start a for loop upto how many widgets you want
3.Appends a widget into a list along with their master value and option values
4.Add them into a window with a suitable layout method
'''

def calc(evt):
    obj=evt.widget
    val=l.cget('text')
    if obj.cget('text')=='=':
        l.config(text=eval(val))
    elif obj.cget('text')=='clr':
        l.config(text=" ")
    else:
        val=val+str(obj.cget('text'))
        l.config(text=val)

w1=Tk()
w1.geometry("300x370+30+40")
w1.config(bg="white")

'''for i in l1[ :1:1]:
    #for j in range(1,4):
    i=Button(w1,text=1)
    i.pack()
        #j=j+1'''

l=Label(w1,width=30,border=2)
l.place(x=45,y=10)

l1=[]
corx1=25
corx2=25
for i in range(10):
    if i<5:
        l1.append(Button(w1,text=i,height=2,width=5))
        l1[i].bind("<Button>",calc)
        l1[i].place(x=corx1,y=50)
        corx1=corx1+50
    else:
        l1.append(Button(w1,text=i,height=2,width=5))
        l1[i].bind("<Button>",calc)
        l1[i].place(x=corx2,y=100)
        corx2=corx2+50    

add=Button(w1,text='+',height=2,width=5)
add.bind("<Button>",calc)
add.place(x=25,y=150)

sub=Button(w1,text='-',height=2,width=5)
sub.bind("<Button>",calc)
sub.place(x=75,y=150)

mul=Button(w1,text='*',height=2,width=5)
mul.bind("<Button>",calc)
mul.place(x=125,y=150)

div=Button(w1,text='/',height=2,width=5)
div.bind("<Button>",calc)
div.place(x=175,y=150)

eq=Button(w1,text='=',height=2,width=5)
eq.bind("<Button>",calc)
eq.place(x=225,y=150)

clr=Button(w1,text="clr",height=2,width=5)
clr.bind("<Button>",calc)
clr.place(x=25,y=200)

