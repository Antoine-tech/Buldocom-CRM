import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Nasaly2110',
    database='Buldocom'  # Specify the database name here
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS Buldocom")

print("All done!")

