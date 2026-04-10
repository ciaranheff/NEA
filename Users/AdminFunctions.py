########## Importing ############
import os
#################################
import json
#################################
import Users.LogIn
UL = Users.LogIn
#################################
import Users.AccountManagment
UA = Users.AccountManagment
#################################
from Questions.Topic import MakeQuestionList
QuestionList,Subjects = MakeQuestionList()

def KeepIn(): # Function to wait for admin to read data before clearing the screen
    out = False
    while out == False:
        out = input("Enter any key to escape")
    os.system("cls") # clears screen to declutter

def GetTopics(): #formats the json data correctly and resets list every time new quiz starts
    Topics = []
    ##### json handling
    with open("TopicQuestions.json","r") as f: #opens json file to read from
        data = json.load(f)
    f.close() #closes json file to allow for edditing inother functions
    #####
    for i in data["Questions"]:
        if (i["Topic"]) not in Topics:#makes a list of all topics by making a list of topics which have already come up and seeing if the current topic value is new or not
            Topics.append(i["Topic"])
    return Topics

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
                print("---Exam Questions---")
                for i in range (len(All)):
                    print(All[i-1])
                print("---Multi Choice---")
                All = (UA.MultiChoiceSaveData())
                for i in range (len(All)):
                    print(All[i-1])
                KeepIn()
            elif ans == '9':
                os.system("cls")
                return()
            else:
                os.system("cls")
                print("invalid respone")

def TopicSpecific():##############
    while True:
        print(f"{Subjects}\nWhat Subject would you like to see (press enter to exit)")
        what = input()
        if what == "":
            return()
        else:
            All = UA.CorrectSubject(what)
            if All != []:
                print("Attempt Number - User - Topic - Correct")
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
            while True:
                what = input(f"---{who}---\n1. All Data \n2. Topic data \n3. Topic Stats\n4. MultiChoice\n9. Return\n")
                os.system("cls")

                if what == '1': #all data
                    print("Data points here")
                    results = (UA.UserAll(who)) #retreaves all data raw from database
                    for i in range (len(results)): #prints each entry on a new line
                        print(results[i])
                    KeepIn()

                elif what == '2':# Minmal data
                    print("Atempt Number - Answer Correct - Topic")
                    results = (UA.UserQuestion(who)) #retreaves 
                    for i in range (len(results)): #prints each entry on a new line
                        print(results[i])
                    KeepIn()

                elif what == '3': #Stats
                    persent = PercentageCorrect(who)
                    for i in persent:
                        print(i)
                    KeepIn()

                elif what == '4':
                    print("Data points here")
                    results = UA.UserMultiChoice(who)
                    for i in range (len(results)): #prints each entry on a new line
                        print(results[i])
                    KeepIn()

                elif what == '9': #Exit
                    os.system("cls")
                    return()
        else: # catch for when user does not exisit
            print("No user Found")

def PercentageCorrect(who):
    percentlist = []
    #### Total ####
    data = UA.UserCorrectAll(who)
    score = 0
    total = len(data)
    for i in data:
        if i[0] == 1:
            score += 1
    if total != 0:
        if score == 0:
            totalpercent = 0
        else:
            totalpercent = float((score/total) * 100)
    else:
        totalpercent = 'NA'
    percentlist.append(['Total',totalpercent])
    #### Topic ####
    Topics = GetTopics()
    for i in Topics:
        score = 0
        data = UA.UserCorrectSubject(who,i)
        total = len(data)
        for j in data:
            if j[0] == 1:
                score += 1
        if total != 0:
            if score == 0:
                topicpercent = 0
            else:
                topicpercent = float((score/total)* 100)
        else:
            topicpercent = 'NA'
        percentlist.append([i,topicpercent])
    return percentlist


#############################################################
def ValidPassword():
    validpassword = False
    while validpassword == False:
        password = input("What is the password (must be 3 or more characters long) ").strip()
        if len(password) >= 3:
            validpassword = True
    return password
    
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
                check = input("Are you sure (Y)").upper() # double checking they want to delete the user
                if check == "Y":
                    UA.DeleteUser(who)
                    print(f"{who} has been deleted")
                    KeepIn()
            else:
                print("Could not find user")
        elif what == "3": # add new User
            name = input("What is the Username ")
            password = ValidPassword()
            admin = input("Is the User an Admin Y/N ").upper()
            os.system("cls")
            UA.AddUser(name,password,admin)
        elif what == "4": #Change User password
            print(UL.GetUserNames())
            who = input("Who's Password do you want to change ")
            if UL.CheckForUser(who) == True:
                newpass = ValidPassword()
                UA.PasswordChange(who,newpass)
                os.system("cls")
                print(f"{who}'s password changed to {newpass}")
            else:
                os.system("cls")
                print("Cannot find User")
        elif what == "5": # Change User Admin status
            print(UL.GetUserNames()) #shows all the usernames
            who = input("Who's admin status do you want to change ")
            if UL.CheckForUser(who) == True:
                admin = False
                while admin != "Y" and admin != "N": #makes sure the admin status is either Y or N
                    admin = input("Do you want to make this user an admin Y/N ").upper()
                UA.AdminChange(who,admin)
                os.system("cls")
                print(f"{who} admin status changed to '{admin}'")
            else:
                os.system("cls")
                print("Could not find User")
        elif what == "9":
            return()

#############################################################################

def EdditingQuestionsMenus():
    while True:
        what = input(f"---Question Edditing---\nWhat are you edditing\n1. Exam questions\n2. Multichoice questions\n9. Exit")
        if what == '1':
            pass
        elif what == '2':
            os.system("cls")
            DisplayMultiChoice()
        elif what == '9':
            return()
        else:
            os.system("cls")

def ExamQuestions():
    pass

def DisplayMultiChoice():
    edditchoice = []
    with open("MultiQuestions.json","r") as f: #opens json file to read from
        data = json.load(f)
    f.close() #closes json file to allow for edditing inother functions
    for i in data["Questions"]: #calls for every dictionary entry
        question_name = (i["Question"]) #gets the dictionary value for i's Question name
        question_number = (i["Number"])#gets the dictionary value for i's Question id
        stuff = [question_name,question_number]
        edditchoice.append(stuff) #makes list of values
    print("Question - Question ID")
    for i in edditchoice:
        print(i)
    which = int(input("What question ID number would you like to edit "))
    for i in edditchoice:
        if which == i[1]:
            print("This question", i)

