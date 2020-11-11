import pyodbc

cnxn = pyodbc.connect(
    'DRIVER={Devart ODBC Driver for ASE};Server=myserver;Port=myport;Database=mydatabase;User ID=myuserid;Password=mypassword;String Types=Unicode')
cursor = cnxn.cursor()
cursor.execute("INSERT INTO EMP (EMPNO, ENAME, JOB, MGR) VALUES (535, 'Scott', 'Manager', 545)")

cursor = cnxn.cursor()
cursor.execute("SELECT * FROM EMP")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
