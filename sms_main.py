import mysql.connector 
conn=mysql.connector.connect(host='localhost',user='root',passwd='WandaVision2800')
c1=conn.cursor()
c1.execute('use SMS;')
print("***********____________School Management System____________***********")
print(" ")
print(" ")
print(" welcome to the menu of School Management System")
print(" ")
print("1. Enrolling For A Course")
print("2. Edit Enrollments (as admin)")
print("3. Display Details")
print("4. Exit")
choice=int(input("Enter the Choice : "))
if choice==1:
    v_admno=int(input("Enter the Admission Number: "))
    v_candidatename=input("Enter your name : ")
    v_course=input("Enter the Course: ")
    if v_course=='JAVA':
        v_course='JAVA'
    elif v_course=='Python':
        v_course='Python'
    elif v_course=='C':
        v_course='C'
    elif v_course=='BASIC':
        v_course='BASIC'
    elif v_course=='HTML':
        v_course='HTML'

    V_SQL_Insert = "insert into cand_details values (" + str(v_admno) + ",'" + v_candidatename +"','" + v_course + "')"
    c1.execute(V_SQL_Insert)
    print(" ")
    print(" You are Enrolled Mr.",v_candidatename,". Congrats!!!")
    conn.commit()
    print(" ")
    print ("Your enrollment for", v_course ,"course is successful!")

if choice==2:
    print("1. Delete An Enrollment")
    print("2. Edit Name")
    print("3. Edit Course")
    print(" ")
    option=int(input("Which of the above options would you like to choose ?: "))
    if option==1:
            change_adm_no=int(input("Enter the admission number of the candidate to be removed:"))
            V_SQL_Insert = "delete from cand_details where adm_no = " + str(change_adm_no) 
            c1.execute(V_SQL_Insert)
            print("")
            conn.commit()
            print("Successfully removed")
    if option==2:
            change_adm_no=int(input("Enter the admission number of the candidate whose name is to be changed:"))
            change_name=input("Enter the desired name:")
            V_SQL_Insert = "update cand_details set candidate_name = '" + change_name + "' where adm_no = " + str(change_adm_no) 
            c1.execute(V_SQL_Insert)
            print("")
            conn.commit()
            print("Successfully edited")
    if option==3:
            change_adm_no=int(input("Enter the admission number of the candidate whose course is to be changed:"))
            change_course=input("Enter the Course: ")
            if change_course=='JAVA':
              change_course='JAVA'
            elif change_course=='Python':
                change_course='Python'
            elif change_course=='C':
               change_course='C'
            elif change_course=='BASIC':
               change_course='BASIC'
            elif change_course=='HTML':
                change_course='HTML'
            V_SQL_Insert = "update cand_details set course_select = '" + change_course + "' where adm_no = " + str(change_adm_no) 
            c1.execute(V_SQL_Insert)
            print("")
            conn.commit()
            print("Successfully modified")
    

if choice==3:
        c1.execute("Select * from cand_details ")
        data=c1.fetchall()
        for row in data:
            print("  Candidates Details ")
            print("  Admission Number : ", row[0])
            print("  Candidate Name   : ", row[1])
            print("  Course Selected  : ", row[2])
            print(" ")
            print(" ")
if choice==4:
    print(' Thank You')  
