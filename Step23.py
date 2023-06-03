import mysql.connector

fpdb = mysql.connector.connect(host="localhost", user="root", password="85BroadStFlamingo!", database="menagerie")
cursor = fpdb.cursor()
select_query = """
SELECT owner, COUNT(*) AS pet_count
FROM pet
GROUP BY owner;
"""
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    owner, pet_count = row
    print(f"Owner: {owner}, Number of Pets:{pet_count}")
cursor.close()
fpdb.close()