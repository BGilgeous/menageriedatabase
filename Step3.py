import mysql.connector

fpdb = mysql.connector.connect(host="localhost", user="root", password="85BroadStFlamingo!")
cursor = fpdb.cursor()
cursor.close()
fpdb.close()