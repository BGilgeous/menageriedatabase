import mysql.connector

fpdb = mysql.connector.connect(host="localhost", user="root", password="85BroadStFlamingo!", database="menagerie")

cursor = fpdb.cursor()
cursor.execute("DESCRIBE pet")
table = cursor.fetchall()
for column in table:
    print(column[0], column[1], column[2], column[3], column[4])
cursor.close()
fpdb.close()