import mysql.connector

fpdb = mysql.connector.connect(host="localhost", user="root", password="85BroadStFlamingo!", database="menagerie")
cursor = fpdb.cursor()
select_query = "SELECT * FROM pet"
cursor.execute(select_query)
rows=cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
fpdb.close()