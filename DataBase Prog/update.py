import mysql.connector as ms

try:
    conn=ms.connect(host='localhost',user='root',password='123456',database='stud')
    cur=conn.cursor()
    q1="update student set name='Bhardwaj',marks=92 where roll=32"
    cur.execute(q1)
    conn.commit()
    conn.close()
except Exception:
    print("Error has occurred.")
else:
    print("Data hs been updated successfuly")
