import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",          # change if needed
    password="Pass123",
    database="inventory_ml"
)

cursor = conn.cursor()
print("MySQL database connected successfully")

conn.close()
