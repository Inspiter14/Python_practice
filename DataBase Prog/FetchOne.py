import mysql.connector as ms

try:
    conn=ms.connect(host="localhost",user="root",password="123456",database="stud")
    cur=conn.cursor()
    cur
