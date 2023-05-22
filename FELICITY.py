import subprocess as sp
import pymysql
import pymysql.cursors

import sys, os


# schedule for felicity
no_of_slots_per_day = 3
slots_per_day = ['10:30:00','15:00:00','17:30:00']
no_of_venue_available_per_day = 4
venue_available_per_day = ['Bakul Warehouse','Amphi','Vindhya','Felicity Ground']


rows, cols = (3, 4)
ttable = [[-1,-1,-1,-1] ,[-1,-1,-1,-1] ,[-1,-1,-1,-1] ,[-1,-1,-1,-1] ]

def schedule_events_from_scratch():
    cur.execute("DELETE FROM SCHEDULE")
    con.commit()  
    
    print("Scheduling tables from scratch : ")
    
    cur.execute("SELECT Event_Number,Event_Name,VENUE,ORGANISED_BY,APPROVED FROM EVENTS")
    con.commit()       
    list_of_dic = cur.fetchall()
    
    print(ttable)
    
    
    for dic in list_of_dic:
        print(dic)
        scheduleEvent(dic=dic)



def check_and_schedule_event():
    eventno = input("Enter the event number of the event you want to schedule :")
    
    cur.execute("SELECT Event_Name,ORGANISED_BY FROM SCHEDULE")
    con.commit()       
    list_of_dic = cur.fetchall()
    
    exit_flag = False
    
    for dic in list_of_dic:
        query = "SELECT Event_Number FROM EVENTS WHERE Event_Name = '"+ dic['Event_Name'] +"' and ORGANISED_BY = '"+ dic['ORGANISED_BY']+"'"
        print(query)
        cur.execute(query)
        con.commit()       
        list_eventno = cur.fetchall()
        
        
        print(list_eventno[0]['Event_Number'],eventno)
        
        if int(list_eventno[0]['Event_Number']) == int(eventno):
            print("ERROR : event is aready scheduled only update is possible")
            exit_flag = True
            break
        
    if exit_flag:
        return
        
    print(exit_flag)
     
    
    cur.execute("SELECT Event_Number,Event_Name,VENUE,ORGANISED_BY,APPROVED FROM EVENTS WHERE Event_number ="+eventno)
    con.commit()       
    list_of_dic = cur.fetchall()
    
    print(list_of_dic)
    print()
    
    scheduleEvent(list_of_dic[0])    


    # print(ttable)
    
def scheduleEvent(dic):    
    
    try :    
        found_empty_slot = False
        place = -1
        time = -1
        
        eventno = dic['Event_Number']
            
        print("for event : "+ str(eventno) + " checking for empty slot ..")
        
        
        for x in range(no_of_slots_per_day):
            for y in range(no_of_venue_available_per_day):
                # print(x,y,ttable[x][y],sep=" , ")
                if ttable[x][y] == -1 :
                    # print("fouifdsfdsdf!!!")
                    ttable[x][y] = eventno
                    found_empty_slot = True
                    place = y
                    time = x
                    break;
            if found_empty_slot :
                break

                
        
        print("slot found :",found_empty_slot)
        
        if(found_empty_slot):
            query = ("INSERT INTO SCHEDULE(Event_Name,TIME,ORGANISED_BY) VALUES('"+ dic['Event_Name'] 
            + "','" +slots_per_day[time]+ "','"+ dic['ORGANISED_BY'] + "')")

            print(query)
            print()
            
            cur.execute(query)
            con.commit()       
            
            query = ("UPDATE EVENTS SET VENUE = '" +venue_available_per_day[place]+ "' WHERE Event_Number = " + str(eventno) + ";")

            print(query)
            print()
            
            cur.execute(query)
            con.commit() 
            
                        
    except Exception as e:
        exception_type, exception_object, exception_traceback = sys.exc_info()
        line_number = exception_traceback.tb_lineno
        
        print("Failed to schedule database")
        print(":---     : ", e)
        print("scheduler error Line number!!!: ", line_number)

#--------------------------------------------------------------
def EnterStudent(): #Inserting Student
    try:
        # Takes student details as input
        # row = {}
        print("Enter student: ")
        name = (input("Name (Fname Middle Lname - Enter NULL if no Middle exists): ")).split(' ')
        First_Name = name[0]
        # print(First_Name)
        Middle_Name = name[1]
        # print(Middle_Name)
        Last_Name = name[2]
        # print(Last_Name)
        while(1):
            Roll_Number = input("Roll Number: ")
            if len(Roll_Number)!=10 or Roll_Number.isdigit()==False:
                print("Error! Enter 10 digit IIITH roll number only.")
                continue
            else:
                break
        # print(Roll_Number)
        DOB = input("Birth Date (YYYY-MM-DD): ")
        # print(DOB)

        query = ("INSERT INTO STUDENTS VALUES('"+First_Name
        + "','"+Middle_Name+ "','"+ Last_Name+ "','"
        + Roll_Number+ "','"+ DOB+ "')")

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterCoordinator():
    try:
        # Takes student details as input
        # row = {}
        print("Select Coordinator From students: ")

        Roll_Number = str(input("Roll Number: "))
        # print(Roll_Number)

        query = ("INSERT INTO COORDINATORS  (COORD_Roll_Number) VALUES (" +Roll_Number+ ")" )

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterEvent():
    try:
        
        print("Enter Event: ")
        
        Event_Name = input("Name :")
                
        while(1):
            EVENT_TYPE = input("Enter event type :")
            if len(EVENT_TYPE) != "cultural" and len(EVENT_TYPE) != "technical" and len(EVENT_TYPE) == "misc":
                print("Error! Enter event type as cultural , technical and misc")
                continue
            else:
                break
        
        ORGANISED_BY = input("ORGANISED_BY :")
        
        SPONSOR = input("SPONSOR :")
        
        COORD_Roll_Number = input("COORD_Roll_Number :")
        
        APPROVED = input("APPROVED :")
        
        query = ("INSERT INTO EVENTS (Event_Name,EVENT_TYPE,ORGANISED_BY,COORD_Roll_Number,APPROVED) VALUES('"
            +Event_Name+"','"+EVENT_TYPE+"','"+ORGANISED_BY+"','"+(COORD_Roll_Number)+"','"+APPROVED+"')")

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")
        
        # to update -----------------------------------------------
        
        
        
        # -----------------------------------------------

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterExpenditure():
    try:
        
        print("Enter Expenditure: ")
        
        Event_Number = input ("Event_Number : ")
        
        query = ("SELECT APPROVED FROM EVENTS WHERE Event_Number = "
                +Event_Number+";")
        
        
        print(query)
        cur.execute(query)
        con.commit()
        
        is_approved = cur.fetchall()
        
        
        if is_approved[0]['APPROVED'] == False:
            print("ERROR : the event has not been approved")
            return
        
        
        FUND_PROPOSED = input ("FUND_PROPOSED : ")
        FUND_RELEASED = input ("FUND_RELEASED : ")
            
        query = ("INSERT INTO EXPENDITURE VALUES("
                +Event_Number+","+FUND_PROPOSED+","+FUND_RELEASED+")")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterIncome(SOURCE_NAME,AMOUNT):
    try:
        
        print("Enter Income: ")      
  
        query = ("INSERT INTO INCOME VALUES('"
                +SOURCE_NAME+"',"+AMOUNT+")")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterSponsors():
    try:
        
        print("Enter Sponsors: ")
        
        SPONSOR_NAME = input("SPONSOR_NAME :")
        AMOUNT = input("AMOUNT :")
        
  
        query = ("INSERT INTO SPONSORS VALUES('"
                +SPONSOR_NAME+"',"+AMOUNT+")")
        
        EnterIncome(SOURCE_NAME=SPONSOR_NAME,AMOUNT=AMOUNT)


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterFoodStall():
    try:
        
        print("Enter FoodStalls: ")
        
        STALL_NAME = input("STALL_NAME :")
        AMOUNT = input("AMOUNT :")
        
  
        query = ("INSERT INTO FOOD_STALLS VALUES('"
                +STALL_NAME+"',"+AMOUNT+")")
        
        EnterIncome(SOURCE_NAME=STALL_NAME,AMOUNT=AMOUNT)
        


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterFoodOps():
    try:
        
        print("Enter Food Options: ")
        
        STALL_NAME = input("STALL_NAME :")
        ITEM = input("ITEM :")
        PRICE = input("PRICE :")
        
  
        query = ("INSERT INTO FOOD_OPTIONS (STALL_NAME, ITEM, PRICE) VALUES('"
                + STALL_NAME + "','" + ITEM + "'," + PRICE + ")")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterEVENT_MANAGERS():
    try:
        
        print("Enter Food Options: ")
        
        Event_Number = input("Event_Number :")
        COORD_Roll_Number = input("COORD_Roll_Number :")

  
        query = ("INSERT INTO EVENT_MANAGERS(Event_Number,COORD_Roll_Number) VALUES('"
                + Event_Number + "'," + COORD_Roll_Number + ")")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterPARTICIPANT_LIST():
    try:
        
        print("Enter Participants: ")
        

        Event_Number = input("Event_Number :")
        Roll_Number = input("Roll_Number :")

  
        query = ("INSERT INTO PARTICIPANT_LIST(Event_Number,Roll_Number) VALUES('"
                + Event_Number + "'," + Roll_Number + ")")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return

def EnterSPONSORED_EVENTS():
    try:
        
        print("Enter events sponsored: ")
        

        Event_Number = input("Event_Number :")
        SPONSOR_NAME = input("SPONSOR_NAME :")
        
        query = ("INSERT INTO SPONSORED_EVENTS(Event_Number,SPONSOR_NAME) VALUES('"
                +Event_Number + "','" + SPONSOR_NAME + "')")


        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return
#--------------------------------------------------------------
def BalSheet():
    #Profit-Loss
    try:
        cur.execute("SELECT SUM(AMOUNT) FROM INCOME")
        result = cur.fetchall()
        cur.execute("SELECT SUM(FUND_RELEASED) FROM EXPENDITURE")
        result1=cur.fetchall()
        Bal=float(result[0]['SUM(AMOUNT)'])-float(result1[0]['SUM(FUND_RELEASED)'])
        print("Income: ",float(result[0]['SUM(AMOUNT)']),"\tExpenditure: ",float(result1[0]['SUM(FUND_RELEASED)']))
        print("Balance: ",Bal)
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(":---     : ", e)
        print()        
        print()

    return 

def ExpByClub():
    #Profit-Loss
    try:
        cur.execute("select EVENTS.ORGANISED_BY , sum(EXPENDITURE.FUND_PROPOSED) FROM EVENTS , EXPENDITURE WHERE EVENTS.Event_Number = EXPENDITURE.Event_Number GROUP BY EVENTS.ORGANISED_BY ;")
        clubs_exp_list = cur.fetchall()
        
        # print(clubs_exp_list)
        
        for dic in clubs_exp_list:
            print("Club: ",dic['ORGANISED_BY'],"has expenses of \t\t:",dic['sum(EXPENDITURE.FUND_PROPOSED)'])
        
       
        
    
    except Exception as e:
        con.rollback()
        print("Failed to acess into database")
        print(":---     : ", e)
        exception_type, exception_object, exception_traceback = sys.exc_info()
        line_number = exception_traceback.tb_lineno
        print("error Line number!!!: ", line_number)
        print()        
        print()

    return 

def StudDetails():
    try:
        print("Check student details available for given name or roll number")
        choice=int(input("Enter choice for querying: \n1: First Name\n2: Roll Number\n"))
        if choice==1:
            name=input("Enter first name to be queried: ")
            query=("SELECT * FROM STUDENTS WHERE first_Name='"
            +name+"'")
        elif choice==2:
            name=input("Enter roll number to be queried: ")
            query=("SELECT * FROM STUDENTS WHERE Roll_Number='"
            +name+"'")
        
        # print(query)
        cur.execute(query)
        res=cur.fetchall()
        # print(res)
        c=0
        print()
        for dic in res:
            c+=1
            print("First Name: ",dic['First_Name'])
            print("Middle Name: ",dic['Middle_Name'])
            print("Last Name: ",dic['Last_Name'])
            print("Roll Number: ",dic['Roll_Number'])
            print("Date of Birth: ",dic['DOB'])
            print()
        print(c,"entries matching")
        roll=res[0]['Roll_Number']
        query=("Select EVENTS.Event_Name from EVENTS"
        +" JOIN PARTICIPANT_LIST ON EVENTS.Event_Number="
        +"PARTICIPANT_LIST.Event_Number where "
        +"PARTICIPANT_LIST.Roll_Number="
        +str(roll))
        # print(query)
        cur.execute(query)
        res=cur.fetchall()
        # print(res)
        print("Events: ")
        c=0
        for dic in res:
            c+=1
            print(dic['Event_Name'])
        if(c==0):
            print("Not participating")
    except Exception as e:
        con.rollback()+"\'"
        print("Failed to read from database")
        print(">>>>>>>>>>>>>", e)

    return

def UpdateTimeVenue():
    try:
        print("Update time or venue of events in schedule")
        choice=int(input("Enter choice for querying: \n1: Time\n2: Venue\n"))
        eno=input("Enter event name: ")
        if choice==1:
            upd=input("Enter time of event to be rescheduled (HH:MM): ")
            query=("UPDATE SCHEDULE SET TIME='"+upd+":00' where "
            +"Event_Name='"+str(eno)+"\'")
        elif choice==2:
            upd=input("Enter venue of event to be rescheduled (): ")
            query=("UPDATE EVENTS SET Venue='"+upd+"' where "
            +"Event_Name='"+str(eno)+"\'")
        
        print(query)
        cur.execute(query) 
        con.commit()  
        
    except Exception as e:
        con.rollback()
        print("Failed to read from database")
        print(">>>>>>>>>>>>>", e)

    return

def showStudent():
    # hj--------------------------
    
    print()
    cur.execute("SELECT * FROM STUDENTS")
    student_data_set = cur.fetchall()
    for dic in student_data_set:
            print("First Name: ",dic['First_Name'])
            print("Middle Name: ",dic['Middle_Name'])
            print("Last Name: ",dic['Last_Name'])
            print("Roll Number: ",dic['Roll_Number'])
            print("Date of Birth: ",dic['DOB'])  
            print() 
    
    print()
    return


    
def showCoordinators():
    # hj--------------------------
    
    print()

def showEvents():
    print()
    
def showFoodStall():
    print()
    
def showSchedule():
    print()
    
def showSponsors():
    print()
    
    
def showData():
    print("Select which data set to view") 
    print("1. Student Records") 
    print("2. Coordinators") 
    print("3. Events") 
    print("4. Schedule") 
    print("5. Sponsors ") 
    
    ch = int(input("Enter choice> ")) 
    
    if(ch == 1):
        showStudent()
    if(ch == 2):
        showCoordinators()
    if(ch == 3):
        showEvents()
    if(ch == 4):
        showSchedule()
    if(ch == 5):
        showSponsors()
    # else:
    #     print("Error: Invalid Option")
    
def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        EnterStudent()
    elif(ch == 2):
        EnterCoordinator()
    elif(ch == 3):
        EnterEvent()
    elif(ch == 4):
        EnterExpenditure()
    elif(ch == 5):
        EnterIncome()
    elif(ch == 6):
        EnterSponsors()
    elif(ch == 7):
        EnterFoodStall()
    elif(ch == 8):
        EnterFoodOps()
    elif(ch == 9):
        EnterEVENT_MANAGERS()
    elif(ch == 10):
        EnterPARTICIPANT_LIST()
    elif(ch == 11):
        EnterSPONSORED_EVENTS()
    elif(ch == 12):
        BalSheet()
    elif(ch == 13):
        ExpByClub()
    # else:
    #     print("Error: Invalid Option")

# -------------------mnu wrapper code----------------------------


def insertMenu():
    print("\t\t->1. Enter Student")
    print("\t\t->2. Enter Coordinator")
    print("\t\t->3. Enter Event")
    print("\t\t->4. Enter Expenditure")
    print("\t\t->5. Enter Sponsors")
    print("\t\t->6. Enter FoodStall")
    print("\t\t->7. Enter Food Options")
    print("\t\t->8. Enter Participants LIST")
    print("\t\t->9. Enter SPONSORED EVENTS")
    
    ch2 = int(input("\t\t->Enter choice> "))
    print("----------------------")    
    print()
    
    if(ch2 == 1):
        EnterStudent()

    elif(ch2 == 2):
       EnterCoordinator()
               

    elif(ch2 == 3):
        EnterEvent()
               

    elif(ch2 == 4):
        EnterExpenditure()
               

    elif(ch2 == 5):
        EnterSponsors()

    elif(ch2 == 6):
        EnterFoodStall()
               
    elif(ch2 == 7):
        EnterFoodOps()
               

    elif(ch2 == 8):
        EnterPARTICIPANT_LIST()
               
               
    elif(ch2 == 9):
        EnterSPONSORED_EVENTS()
        
    else    :
        print("invalid option")
 
def updateMenu():
    print("\t\t->1. Time or venue of scheduled event")
    print("\t\t->2. Event Coordinator ")


    
    ch2 = int(input("\t\t->Enter choice> "))
    print("----------------------")    
    print()
    
    if(ch2 == 1):
        UpdateTimeVenue()

    elif(ch2 == 2):
        print("implentm !!!!!!")
                       
    else    :
        print("invalid option")
     
def deleteMenu():
    print("\t\t->1. Delete Student")
    print("\t\t->2. Delete Coordinator")
    print("\t\t->3. Delete Event")
    print("\t\t->4. Delete Event Participants")
    print("\t\t->5. Delete Income Source (Stall/Sponsor)")


    
    ch2 = int(input("\t\t->Enter choice> "))
    print("----------------------")    
    print()
    
    if(ch2 == 1):
        UpdateTimeVenue()

    elif(ch2 == 2):
        print("implentm !!!!!!")
    elif(ch2 == 3):
        print("implentm !!!!!!")
    elif(ch2 == 4):
        print("implentm !!!!!!")
    elif(ch2 == 5):
        print("implentm !!!!!!")
                       
    else    :
        print("invalid option")


# -----------------------------------------------------------


# Global
while(1):
    #tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    # username = input("Username: ")
    # password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host="localhost",
                              #port=30306,
                              user="root",
                              password="Suresh@2018",
                              db="FELICITY",
                              cursorclass=pymysql.cursors.DictCursor)


        if(con.open):
            print("Connected to Felicity dbms")
        else:
            print("Failed to connect")


        with con.cursor() as cur:
            while(1):

                
                print("1. Retrieval")
                print("2. Analysis")
                print("3. Modify")

                ch1 = int(input("Enter choice> "))
                print()
                print()

                if(ch1 == 1):
                    print("\t1. Selection of Data")
                    print("\t2. Projection")
                    print("\t3. Search student (with name/roll number)")  
                    print("\t4. Auto Scheduler") 
                    print("\t5. Auto Scheduler for individual events") 
                    print("\t6. Net revenue(include Aggregation)")
                    
                    
                    ch2 = int(input("\tEnter choice> "))
                    print("----------------------")    
                    print()
                    
                    if(ch2 == 1):
                        showData()
                    
                    if(ch2 == 2):
                        # show()
                        print("---")
                        
                    if(ch2 == 3):
                        StudDetails() 
                    
                    if(ch2 == 4):
                        schedule_events_from_scratch()
                        
                    if(ch2 == 5):
                        check_and_schedule_event()
                    
                    if(ch2 == 6):
                        BalSheet()
                        
                    
                if(ch1 == 2):
                    print("\t1. Net revenue")
                    print("\t2. Expenditure by each club on events")

                    
                    ch2 = int(input("\tEnter choice> "))
                    print("----------------------")    
                    print()
                    
                    if(ch2 == 1):
                        BalSheet()
                    
                    if(ch2 == 2):
                        ExpByClub()
                    
                    
                    
                if(ch1 == 3):
                    print("\t1. Insert Data")
                    print("\t2. Updation")
                    print("\t3. Delete Data")

                    
                    ch2 = int(input("\tEnter choice> "))
                    print("----------------------")    
                    print()
                    
                    if(ch2 == 1):
                        insertMenu()
                    
                    if(ch2 == 2):
                        updateMenu()
                    
                    if(ch2 == 3):
                        deleteMenu()
                    
                    
                    
                
  #              tmp = sp.call('clear', shell=True)
                if ch1 == -1:
                    exit()
                else:
                    tmp = input("Enter any key to CONTINUE>")
                    print()
                    print()
                    print()
                    print()

    except Exception as e:
    #    tmp = sp.call('clear', shell=True)
        print(e)
        print("EROOR Detected conecntion re-esatblish")
        
        exception_type, exception_object, exception_traceback = sys.exc_info()
        line_number = exception_traceback.tb_lineno
        print("error Line number!!!: ", line_number)

        print("Exception type: ", exception_type)
        filename = exception_traceback.tb_frame.f_code.co_filename
        tmp = input("Enter any key to CONTINUE>")
