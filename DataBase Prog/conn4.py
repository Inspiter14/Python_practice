import mysql.connector as ms

con=ms.connect(host="localhost",user="root",password="Aditya@1007",database="hms")

cur=con.cursor()
q1="select * from rooms"
cur.execute(q1)
data1=cur.fetchall()
print(data1)
for data in data1:
    print("Room no " ,data[0])
    print("Name ",data[1])
    print("Charges ", data[2])
