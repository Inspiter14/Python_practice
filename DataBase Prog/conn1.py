import mysql.connector as ms

con=ms.connect(host="localhost",user="root",password="Aditya@1007",database="hms")

cur=con.cursor()
q1="insert into rooms values(101,'delux',5000)"
cur.execute(q1)
con.commit()

