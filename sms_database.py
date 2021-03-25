import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',passwd='apkotwacb')
if conn.is_connected():
  print("Successfully Connected")
c1=conn.cursor()
c1.execute('create database SMS')
print ('Database created')

