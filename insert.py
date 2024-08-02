import mysql.connector as ms

try:
    conn=ms.connect(host="localhost",user="root",password="12\3456",database="stud")
    cur=conn.cursor()
    q1="insert into student values (24,'Nikita',85)"
    cur.execute(q1)
    conn.commit()
    conn.close()
except:
    print("Error has occurrred")
else:
    print("Data has been inserted successfully")
