import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="04harsh",
  database="joins"
)

mycursor = mydb.cursor()
mycursor.execute("create table py6 (name varchar(10), address varchar(50))")
sql = "INSERT INTO py6 (name, address) VALUES (%s, %s)"
val = [
  ('sam', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('henry', 'Central st 954'),
  ('dwayne', 'Main Road 989'),
  ('Veronica', 'Sideway 1633')
]

mycursor.executemany(sql, val)
mydb.commit()
# print(mycursor.rowcount, "was inserted.")
mycursor.execute("select * from py6")
print("Table Contents")
res=mycursor.fetchall()
for x in res:
    print(x)
print(mycursor.rowcount, "record inserted.")

sql4 = "update py6 set address='Mumbai' where name='Veronica'"
sql5 = "update py6 set address='Delhi' where name='dwayne'"

mycursor.execute(sql4)
mycursor.execute(sql5)
print("")

mydb.commit()
mycursor.execute("select * from py6")
print("Updated Table Contents")
res=mycursor.fetchall()
for x in res:
    print(x)
print(mycursor.rowcount, "record inserted.")
