import mysql.connector as sql
conn = sql.connect(host="localhost",user="root",passwd="satyam",database="mydb")
if conn.is_connected() == True:
    print("Connection built")
    cur = conn.cursor()
    cur.execute("Select * from emp")
    for i in cur:
        print(i)
else:
    print("Error")