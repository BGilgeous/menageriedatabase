import mysql.connector

fpdb = mysql.connector.connect(host="localhost", user="root", password="85BroadStFlamingo!")

cursor = fpdb.cursor()
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()

for database in databases:
    print(database[0])
cursor.close()
fpdb.close()