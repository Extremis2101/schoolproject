import mysql.connector 
conn=mysql.connector.connect(host='localhost',user='root',passwd='apkotwacb')
if conn.is_connected():
  print("Successfully Connected")
c1=conn.cursor()
c1.execute('use SMS;')
c1.execute('create table cand_details(adm_no int primary key, candidate_name varchar(50), course_select varchar(20));')
print ('Table created')
