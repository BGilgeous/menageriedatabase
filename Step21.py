import mysql.connector

fpdb = mysql.connector.connect(host="localhost", user="root", password="85BroadStFlamingo!", database="menagerie")
cursor = fpdb.cursor()
select_query = "SELECT name, birth FROM pet;"
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    name,birth = row
    print(f"Name: {name}, Birth:{birth}")
cursor.close()
fpdb.close()
