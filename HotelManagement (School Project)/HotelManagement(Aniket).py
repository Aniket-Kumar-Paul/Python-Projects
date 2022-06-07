x=input('Enter MySQL user: ')
y=input('Enter MySQL password: ')

import mysql.connector as mc
conn=mc.connect(host='localhost',user=x,passwd=y)
stmt=conn.cursor()

#tables

print()
print()
x=input('Have you used this software before (On this computer) ? (Y/N) :- ')
if (x in ['N','n']):
    print('Creating the database . please wait ...')
    stmt.execute('Create database HotelManagement;')
    stmt.execute('use HotelManagement;')
    stmt.execute('create table workanddept(work varchar(20) primary key,dept varchar(15),salary_per_month int);')
    stmt.execute('create table employee(e_name varchar(20) primary key,gender varchar(1),work varchar(20) references workanddept(work));')
    stmt.execute('create table roomfacilities(F_no int primary key,facilities varchar(30),cost_per_day int);')
    stmt.execute('create table rooms(room_no int primary key,F_no int references roomfacilities(F_no),Booking_status varchar(15));')
    stmt.execute('''create table customers(c_no int primary key,customer_name varchar(20),Gender varchar(1),Phone_no varchar(15),
    Address varchar(70),check_in date,check_out date default NULL,no_of_days int default NULL,total_amount int default NULL,room_no int references rooms(room_no));''')

    stmt.execute("insert into workanddept values('Food Deliver','Food',20000)")
    stmt.execute("insert into workanddept values('Manager','Management',60000)")
    stmt.execute("insert into workanddept values('Supervisor','Management',55000)")
    stmt.execute("insert into workanddept values('Accontant','Management',50000)")
    stmt.execute("insert into workanddept values('Chef','Food',30000);")
    stmt.execute("insert into workanddept values('Lift Man','Lift',25000);")
    stmt.execute("insert into workanddept values('Guard','Security',28000);")
    stmt.execute("insert into workanddept values('Receptionist','Reception',40000);")

    stmt.execute("insert into employee values('Nitesh','M','Chef');")
    stmt.execute("insert into employee values('Sazad','M','Supervisor');")
    stmt.execute("insert into employee values('Aniket','M','Manager');")
    stmt.execute("insert into employee values('Ayush','M','Accountant');")
    stmt.execute("insert into employee values('Dipti','F','Receptionist');")
    stmt.execute("insert into employee values('Kasak','F','Receptionist');")
    stmt.execute("insert into employee values('Sanjiv','M','Guard');")
    stmt.execute("insert into employee values('Irfan','M','Guard');")
    stmt.execute("insert into employee values('Mayank','M','Lift Man');")
    stmt.execute("insert into employee values('Rajiv','M','Food Deliver');")

    stmt.execute("insert into roomfacilities values(01,'Single Bed(NON AC)',3000);")
    stmt.execute("insert into roomfacilities values(02,'Double Bed(NON AC)',5000);")
    stmt.execute("insert into roomfacilities values(03,'Single Bed(AC)',7000);")
    stmt.execute("insert into roomfacilities values(04,'Double Bed(AC)',8500);")

    stmt.execute("insert into rooms values(01,01,'Unbooked');")
    stmt.execute("insert into rooms values(02,01,'Unbooked');")
    stmt.execute("insert into rooms values(03,01,'Unbooked');")
    stmt.execute("insert into rooms values(04,01,'Unbooked');")
    stmt.execute("insert into rooms values(05,01,'Unbooked');")
    stmt.execute("insert into rooms values(06,02,'Unbooked');")
    stmt.execute("insert into rooms values(07,02,'Unbooked');")
    stmt.execute("insert into rooms values(08,02,'Unbooked');")
    stmt.execute("insert into rooms values(09,02,'Unbooked');")
    stmt.execute("insert into rooms values(10,02,'Unbooked');")
    stmt.execute("insert into rooms values(11,03,'Unbooked');")
    stmt.execute("insert into rooms values(12,03,'Unbooked');")
    stmt.execute("insert into rooms values(13,03,'Unbooked');")
    stmt.execute("insert into rooms values(14,03,'Unbooked');")
    stmt.execute("insert into rooms values(15,03,'Unbooked');")
    stmt.execute("insert into rooms values(16,04,'Unbooked');")
    stmt.execute("insert into rooms values(17,04,'Unbooked');")
    stmt.execute("insert into rooms values(18,04,'Unbooked');")
    stmt.execute("insert into rooms values(19,04,'Unbooked');")
    stmt.execute("insert into rooms values(20,04,'Unbooked');")

    conn.commit()

    print()
    print()
    print('Done!!')
elif (x in ['Y','y']):
    stmt.execute('use HotelManagement;')
else:
    exit()

    
    



#Functions:-

#1.Show Table Functions

def showwad():
    print('(WORK        , DEPT      , SALARY_PER_MONTH  )')
    print()
    stmt.execute('select * from workanddept;')
    x=stmt.fetchall()
    for i in x:
        print(i)
def showe():
    print('(E_NAME    , GENDER, WORK )')
    print()
    stmt.execute('select * from employee;')
    x=stmt.fetchall()
    for i in x:
        print(i)
def showrf():
    print("(F_NO , FACILITIES       ,COST_PER_DAY)")
    print()
    stmt.execute('select * from roomfacilities;')
    x=stmt.fetchall()
    for i in x:
        print(i)
def showr():
    print('(ROOM_NO , F_NO , BOOKING_STATUS)')
    print()
    stmt.execute('select * from rooms;')
    x=stmt.fetchall()
    for i in x:
        print(i)
def showc():
    print('(C_NO , CUSTOMER_NAME       , GENDER ,PHONE_NO    ,ADDRESS  , CHECK_IN  , CHECK_OUT  , NO_OF_DAYS , TOTAL_AMOUNT ,ROOM_NO )') 
    print()
    stmt.execute('select * from customers;')
    x=stmt.fetchall()
    for i in x:
        print(i)


#2.updateSalary Function for workanddept table

def updatesalary():
    x=input('Enter Work: ')
    y=int(input('Enter new salary: '))
    stmt.execute("update workanddept set salary_per_month={} where work='{}'".format(y,x))
    conn.commit()
    print('Salary Updated Successfully!!!')

#3.addemployee,deleteemployee,updateemployee Functions for employee table

def adde():
    x=input('Enter Employee name: ')
    y=input('Gender(M/F): ')
    z=input('Work: ')
    stmt.execute("insert into employee values('{}','{}','{}');".format(x,y,z))
    conn.commit()
    print('New Entry successfull!!!')
def deletee():
    x=input('Enter employee name to delete: ')
    stmt.execute("delete from employee where e_name='{}';".format(x))
    conn.commit()
    print('Deletion successfull!!!')
def updatee():
    x=int(input('Enter option: \n 1.Update Name \n 2.Update Gender \n 3.Update Work \n :-'))
    a=input('Enter current employee name: ')
    if (x==1):
        b=input('Enter new name: ')
        stmt.execute("update employee set e_name='{}' where e_name='{}';".format(b,a))
        conn.commit()
        print('Done!!')
    elif(x==2):
        b=input('Enter new gender(M/F): ')
        stmt.execute("update employee set gender='{}' where e_name='{}';".format(b,a))
        conn.commit()
        print('Done!!')
    else:
        b=input('Enter new work: ')
        stmt.execute("update employee set work='{}' where e_name='{}';".format(b,a))
        conn.commit()
        print('Done!!')

#4.updatefacilitycost function for roomfacilities table

def updatefacilitycost():
   x=int(input('Enter F_no: '))
   y=int(input('Enter new cost_per_day: '))
   stmt.execute("update roomfacilities set cost_per_day={} where F_no={};".format(y,x))
   conn.commit()
   print('Done!!')

#5.book/unbook function for rooms table

def book(r_no):
    stmt.execute("update rooms set Booking_status='Booked' where room_no={};".format(r_no))
    conn.commit()
def unbook(r_no):
    stmt.execute("update rooms set Booking_status='Unbooked' where room_no={};".format(r_no))
    conn.commit()

#6.addcustomer,checkout function for customers table

def addc():
    a=int(input('Enter c_no: '))
    b=input('Enter Customer name: ')
    c=input('Enter Gender(M/F): ')
    d=int(input('Enter Phone no.: '))
    e=input('Enter Address: ')
    f=input('Enter Check-in-date(YYYY-MM-DD): ')
    stmt.execute('select * from roomfacilities;')
    x=stmt.fetchall()
    for i in x:
        print(i)
    g=int(input("Enter Required Facility's F_no(01,02,03,04): "))
    stmt.execute("select room_no from rooms r,roomfacilities rf where (r.F_no=rf.F_no) and (r.F_no ={}) and (Booking_status='Unbooked');".format(g))
    y=stmt.fetchall()
    for j in y:
        print(j)
    h=int(input("Enter any room no.: "))
    stmt.execute("insert into customers(c_no,customer_name,Gender,Phone_no,Address,check_in,room_no) values({},'{}','{}',{},'{}','{}',{});".format(a,b,c,d,e,f,h))
    conn.commit()
    print()
    print(b,'Your Room no. is',h)
    book(h)
def checkout():
    a=int(input('Enter c_no: '))
    b=input('Enter Check-out-date(YYYY-MM-DD): ')
    stmt.execute("update customers set check_out='{}' where c_no={};".format(b,a))
    conn.commit()
    stmt.execute('select date(check_out)-date(check_in) from customers where c_no={};'.format(a))
    x=stmt.fetchall()
    c=x[0][0]
    stmt.execute('select room_no from customers where c_no={};'.format(a))
    y=stmt.fetchall()
    z=y[0][0]
    stmt.execute('select cost_per_day from rooms r,roomfacilities rf where (r.F_no=rf.F_no) and (room_no={});'.format(z))
    p=stmt.fetchall()
    q=p[0][0]
    d=c*q
    stmt.execute("update customers set no_of_days={} where c_no={};".format(c,a))
    conn.commit()
    stmt.execute("update customers set total_amount={} where c_no={};".format(d,a))
    conn.commit()
    unbook(z)
    print('Amount to be paid is Rs.',d)



# Final Program


print()
print()
print("                                                                 WELCOME  TO                                            ")
print()
print("                                                           ....5  *STAR*  HOTEL....                                     ")
print()
print("                                                              MANAGEMENT  SYSTEM                                        ")
print()
print("Developed by: \n Aniket Kumar Paul \n(XII-Sci..KV_Hasimara..)")
print()
print()
print()
p=input('Enter Password: ')
password='123456'
if (p==password):
    pass
else:
    print('Wrong Password!!  Program exiting...')
    input()
    exit()

    
def repeat():
    while True:
        print()
        print()
        a=int(input("Enter any option(1/2/3/4/5/6): \n 1.Work and Department \n 2.Employee \n 3.Room Facilities \n 4.Customers \n 5.Execute own SQL code(NO O/P) \n 6.Quit Program \n :- "))
        print()
        print()
        if (a==1):
            i=int(input('Enter any option: \n 1.See Table Contents \n 2.Update Salary \n :-'))
            print()
            print()
            if (i==1):
                showwad()
                repeat()
            elif (i==2):
                updatesalary()
                repeat()
            else:
                print('Invalid Option')
                repeat()
        elif (a==2):
            i=int(input('Enter any option: \n 1.See Table Contents \n 2.Add Employee \n 3.Delete Employee \n 4.Update Employee Details \n :-'))
            print()
            print()
            if (i==1):
                showe()
                repeat()
            elif (i==2):
                adde()
                repeat()
            elif (i==3):
                deletee()
                repeat()
            elif (i==4):
                updatee()
                repeat()
            else:
                print('Invalid Option')
                repeat()
        elif (a==3):
            i=int(input('Enter any option: \n 1.See Table Contents \n 2.Update Facility Cost \n :-'))
            print()
            print()
            if (i==1):
                showrf()
                repeat()
            elif (i==2):
                updatefacilitycost()
                repeat()
            else:
                print('Invalid Option')
                repeat()
        elif (a==4):
            i=int(input('Enter any option: \n 1.See Table Contents \n 2.Add Customers \n 3.Check_Out \n :-'))
            print()
            print()
            if(i==1):
                showc()
                repeat()
            elif(i==2):
                addc()
                repeat()
            elif(i==3):
                checkout()
                repeat()
            else:
                print('Invalid Option')
                repeat()
        elif(a==5):
            x=input('Enter your SQL code: \n')
            stmt.execute(x)
            print('Done !!')
        elif (a==6):
            exit()
        else:
            print('Invalid Option')
            repeat()

repeat()



    
conn.commit()
conn.close()

print()
print()
print()

print('Press Enter to exit :) ')

input()

# ...The End...
# ...Thank You...
