########## Importing ############
import os
#################################
import Users.LogIn
UL = Users.LogIn
#################################
import Users.AccountManagment
UA = Users.AccountManagment
#################################

Subjects = ['A']

def KeepIn(): # Function to wait for admin to read data before clearing the screen
    out = False
    while out == False:
        out = input("Enter any key to escape")
    os.system("cls") # clears screen to declutter

def AdminResultsSearch():
    while True:
            print(f"---Search Menu---\nWhat kind of data do you want:\n1. User specific\n2. Topic specific\n3. All Data\n9. Return")
            ans = input()
            if ans == '1':
                os.system("cls") # clears screen
                UserSpecific()
            elif ans == '2':
                TopicSpecific()
            elif ans == '3':
                os.system("cls")
                All = (UA.SaveData())
                for i in range (len(All)):
                    print(All[i-1])
                KeepIn()
            elif ans == '9':
                os.system("cls")
                return()
            else:
                print("invalid respone")

def TopicSpecific():
    while True:
        print(f"{Subjects}\nWhat Subject would you like to see (press enter to exit)")
        what = input()
        if what == "":
            return()
        else:
            All = UA.CorrectSubject(what)
            if All != []:
                print("Attempt Number - User - Topic - Remake code - Answer given - Correct")
                for i in range(len(All)):
                    print(All[i-1])
                KeepIn()
            else:
                print("Could not find Topic")
                return()

def UserSpecific():
    while True:
        print(UL.GetUserNames())
        who = input("Whos data do you want to find (press enter to exit)")
        os.system("cls")
        if who == "": #exit state
            os.system("cls")
            return()
        elif UL.CheckForUser(who) == True: # makes sure user exsists
            what = input(f"---{who}---\n1. All Data \n2. Minimal data \n3. User Stats\n9. Return\n")
            os.system("cls")

            if what == '1': #all data
                print("Data points here")
                results = (UA.UserAll(who)) #retreaves all data raw from database
                for i in range (len(results)): #prints each entry on a new line
                    print(results[i])
                KeepIn()

            elif what == '2':# Minmal data
                print("Correct Answer - Answer Given - Remake code")
                results = (UA.UserQuestion(who)) #retreaves (answer given correct answer and remakecode) from database @@@ change temp1 to 'who'
                for i in range (len(results)): #prints each entry on a new line
                    print(results[i])
                KeepIn()

            elif what == '3': #Stats
                persent = PercentageCorrect(who)
                for i in range (len(persent)):
                    print(persent[i-1])
                KeepIn()

            elif what == '9': #Exit
                os.system("cls")
                return()
        else: # catch for when user does not exisit
            print("No user Found")

def PercentageCorrect(who):
    Percentages = [] # list of all percentages
    ################## Works out All subjects ###########################
    list = UA.UserCorrectAll(who) # finds all answers for a user
    correct = 0
    total = len(list)
    for i in range (total):
        if (list[i]) == ('Y',): #checks to see if any given answer is correct
            correct += 1
    try:
        totalpercent = float((correct/total)*100) #finds percentage correct
    except: # error catch for when someone has not done a subject question to prevent 0 devision
        totalpercent = 'NA'
    Percentages.append(('total',totalpercent)) # adds percentage correct and subect to the percentages list
    ################### Works out subject specific ################
    for i in range (len(Subjects)): # for each subject do the loop
        list = UA.UserCorrectSubject(who,(Subjects[i-1])) # finds answers given for any given subject
        correct = 0
        total = len(list)
        for i in range (total):
            if (list[i]) == ('Y',): #checks to see if any given answer is correct
                correct += 1
        try:
            percent = float((correct/total)*100) #finds percentage correct
        except: # error catch for when someone has not done a subject question to prevent 0 devision
            percent = 'NA'
        Percentages.append((Subjects[i-1],percent)) # adds percentage correct and subect to the percentages list
    return(Percentages) # returns the subject list

#############################################################

def AdminAccountManagment():
    while True:
        print(f"---Account Managment--- \n1.Show All User Data\n2.Delete User\n3.Add User\n4.Change Password\n5.Change Admin Status\n9.Exit")
        what = input()
        os.system("cls")
        if what == "1": #shoe all user data
            List = UA.ShowAll() # gets all data from the Users.db database
            print("Username - Password - Admin")
            for i in range (len(List)): # separates the data given
                print(List[i-1])
            KeepIn()
        elif what == "2": # delete user
            print(UL.GetUserNames())
            who = input("Who's account do you want to delete?: ")
            if UL.CheckForUser(who) == True:
                check = input("Are you sure (Y)") # double checking they want to delete the user
                if check == "Y":
                    UA.DeleteUser(who)
                    print(f"{who} has been deleted")
                    KeepIn()
            else:
                print("Could not find user")
        elif what == "3": # add new User
            name = input("What is the Username ")
            password = input("What is the password ")
            admin = input("Is the User an Admin Y/N (case sensative) ")
            os.system("cls")
            UA.AddUser(name,password,admin)
        elif what == "4": #Change User password
            print(UL.GetUserNames())
            who = input("Who's Password do you want to change ")
            if UL.CheckForUser(who) == True:
                newpass = input("What is the new password ")
            else:
                os.system("cls")
                print("Cannot find User")
        elif what == "5": # Change User Admin status
            print(UL.GetUserNames()) #shows all the usernames
            who = input("Who's admin status do you want to change ")
            if UL.CheckForUser(who) == True:
                admin = False
                while admin != "Y" and admin != "N":
                    admin = input("Is this user an admin Y/N ")
                UA.AdminChange(who,admin)
            else:
                os.system("cls")
                print("Could not find User")
        elif what == "9":
            return()