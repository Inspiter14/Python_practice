import mysql.connector as ms

try:
    conn=ms.connect(host="localhost",user="root",password="123456",database="stud")
    cur=conn.cursor()
    q1="delete from student where roll=32"
    cur.execute(q1)
    conn.commit()
    conn.close()
except:
    print("Error has occurred.")
else:
    print("Data has been deleted seccessfully.")
