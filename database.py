import pyodbc 

conn = pyodbc.connect(r'Driver={Microsoft Access Driver(*.mdb, *.accdb %s)};DBQ=C:\Users\Admin\Desktop\ProgrammingLang\python\pythonLinkwithDatabase\database.accdb') 

cursor = conn.cursor()
cursor.execute('select * from database')

for row in cursor.fetchall():
    print (row) 