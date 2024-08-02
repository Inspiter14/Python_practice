m1=int(input("Enter Marks of Math: "))
m2=int(input("Enter Marks of Science: "))
m3=int(input("Enter Marks of History: "))
m4=int(input("Enter Marks of Geog: "))
m5=int(input("Enter Marks of Marathi: "))

per=float(((m1+m2+m3+m4+m5)*100)/400)
print("Percentage is ",per,"%")

if per>=75:
    print("Distinction")
elif per<75 and per>=60:
    print("First Class")
elif per<60 and per>=50:
    print("Second Class")
elif per<50 and per>=40:
    print("Pass")
else:
    print("Fail")
