import mysql.connector as connector

mydb = connector.connect(
    host="localhost",
    user="Admin",
    password="AdminPassword",
    database="listening"
)
mycursor = mydb.cursor(buffered=True, dictionary=True)
print(mydb)
