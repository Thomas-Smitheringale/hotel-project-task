def searchFile(file,target,location):
    f=open(file,"r")
    f.readline()
    line=f.readline()
    while line:
        data=line.split(",")
        if target==data[location]:
            f.close()
            return data
        line=f.readline()
    f.close()
    return "Not found"

def addToFile(file,line):
    f=open(file,"a")
    f.write(line+",\n")
    f.close()


def removeFromFile(file,target,location):
    f=open(file,"r")
    line=f.readline()
    found=line
    line=f.readline()
    while line:
        data=line.split(",")
        if target[location]!=data[location]:
            found=found+line
        line=f.readline()
    f.close()
    f=open(file,"w")
    f.write(found)
    
def login(): #If username and password correct, return True, else return False.
    username=input("ENTER USERNAME: ")
    password=input("ENTER PASSWORD: ")
    data=searchFile("logins.txt",username,0)
    if data=="Not found":
        return False
    elif password==data[1]:
        return True
    return False


def guests():
    loop=True
    while loop:
        option=input("""Would you like to:
1:View guest info
2:Add guest info
3:Remove guest info
4:Return to main menu
>""")
        if option=="1":
            viewGuest()
        elif option=="2":
            addGuest()
        elif option=="3":
            removeGuest()
        elif option=="4":
            loop=False


def viewGuest():
    search=input("Enter name of guest to search for: ")
    guest=searchFile("guests.txt",search,0)
    if guest=="Not found":
        print("Guest not found.")
    else:
        print("""Name: {}
Date of Birth: {}
Room Booked: {}
Bill: {}""".format(guest[0],guest[1],guest[2],guest[3]))
        if len(guest)>5:
            print("Services:")
            for i in range(5,len(guest)):
                print(guest[i-1])
def addGuest():
    #details=input("Enter forename and surname: ")+","
    valid=False
    while not valid:
        valid=True
        try:
            date=input("Enter date of birth in format DD/MM/YY: ")
            date=date.split("/")
            for i in date:
                if valid:
                    if not (len(i)==2 and i.isnumeric() and len(date)==3):
                        print("Invalid date.1")
                        valid=False
            if (int(date[1])>12 or int(date[1])<1) and valid:
                print("Invalid date.2")
                valid=False
            elif (int(date[0])>31 or int(date[0])<1) and valid:
                print("Invalid date.3")
                valid=False
            elif int(date[2])<0 and valid:
                print("Invalid date.4")
                valid=False
        except:
            if valid:
                print("Invalid date.5")
            valid=False
    details=details+date+","
    room=input("Which room was booked: ")
    details=details+room+","
    details=details+"0,"
    services=input("""Which services were booked?
1:Breakfast
2:Dinner
3:Tea
4:Cleaner
Enter booked services like this: 1,3,4
>""")
    if "1" in services:
        print("Breakfast added!")
        details=details+"breakfast,"
    if "2" in services:
        print("Dinner added!")
        details=details+"dinner,"
    if "3" in services:
        print("Tea added!")
        details=details+"tea,"
    if "4" in services:
        print("Cleaner added!")
        details=details+"cleaner,"
    addToFile("guests.txt",details)
        
## MAIN PROGRAM ##

##while not login():
##    print("ACCESS DENIED.")
##    print()
print("ACCESS GRANTED.")
print("""Welcome to the
<<>> <<>> <<>>
 Artemis Hotel
<<>> <<>> <<>>
management system.""")
loggedIn=True
while loggedIn:
    option=input("""-----------
 MAIN MENU
-----------
Would you like to:
1:Guests
2:Rooms
3:Payment
4:Logout
>""")
    if option=="1":
        guests()
    elif option=="2":
        rooms()
    elif option=="3":
        payment()
    elif option=="4":
        loggedIn=False
