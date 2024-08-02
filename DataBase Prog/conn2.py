import mysql.connector as ms

con=ms.connect(host="localhost",user="root",password="Aditya@1007",database="hms")

rno=int(input("ENTER A ROOOM NO"))
typ=input("Enter a room type")
charges=float(input("Enter a charges"))

val=(rno,typ,charges)

cur=con.cursor()
q1="insert into rooms values(%s,%s,%s)"
cur.execute(q1,val)
con.commit()

