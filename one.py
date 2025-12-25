

import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=RAVANA-PC;"
    "DATABASE=Dev;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()
cursor.execute("SELECT * from employee")

rows = cursor.fetchall()   # fetch ALL rows

for row in rows:
    print(row)


conn.close()

