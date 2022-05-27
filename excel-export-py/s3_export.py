# (A) INIT
# (A1) LOAD MODULES
import sqlite3, os, openpyxl
from sqlite3 import Error

# (A2) SETTINGS
DBFILE = "users.db"

# (B) OPEN DATABASE & CREATE EXCEL
conn = sqlite3.connect(DBFILE)
cursor = conn.cursor()
book = openpyxl.Workbook()
sheet = book.active

# (C) EXPORT DATA TO EXCEL
cursor.execute("SELECT * FROM `users`")
results = cursor.fetchall()
i = 0
for row in results:
  i += 1
  j = 1
  for col in row:
    cell = sheet.cell(row = i, column = j)
    cell.value = col
    j += 1

# (D) SAVE EXCEL FILE & CLOSE DB
book.save("demo.xlsx")
conn.close()
