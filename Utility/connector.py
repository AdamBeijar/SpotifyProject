import mysql.connector as connector

mydb = connector.connect(
    host=HOST,
    user=PROFILE,
    password=PROFILE_PASSWORD,
    database=DATABASE
)
mycursor = mydb.cursor(buffered=True, dictionary=True)
print(mydb)
