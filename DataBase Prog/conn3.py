import mysql.connector as ms

con=ms.connect(host="localhost",user="root",password="123456",database="emp")

cur=con.cursor()
q1="select * from employee where id=107"
cur.execute(q1)
data=cur.fetchone()
print("Room no " ,data[0])
print("Name ",data[1])
print("Charges ", data[2])
'''
while True:
    data=cur.fetchone()
    if data==None:
        break
    print("Room no " ,data[0])
    print("Name ",data[1])
    print("Charges ", data[2])

'''
