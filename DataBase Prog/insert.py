import mysql.connector as ms

conn=ms.connect(host="localhost",user="root",password="123456",database="stud")
cur=conn.cursor()
q1="insert into student values (24,'Nikita',85)"
cur.execute(q1)
conn.commit()
