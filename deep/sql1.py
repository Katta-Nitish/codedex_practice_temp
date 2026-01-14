import mysql.connector
database=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="nitish"
    )
cb=database.cursor()
print(cb.execute("desc student;"))
database.close()

