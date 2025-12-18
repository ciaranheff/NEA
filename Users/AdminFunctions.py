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
                out = False
                print("Data points here")
                results = (UA.UserAll(who)) #retreaves all data raw from database
                for i in range (len(results)): #prints each entry on a new line
                    print(results[i])
                while out == False: #makes it easier to see data by clearing everything and waiting till user wants to move on
                    out = input("Enter any key to escape")
                os.system("cls")

            elif what == '2':# Minmal data
                out = False
                print("Correct Answer - Answer Given - Remake code")
                results = (UA.UserQuestion(who)) #retreaves (answer given correct answer and remakecode) from database @@@ change temp1 to 'who'
                for i in range (len(results)): #prints each entry on a new line
                    print(results[i])
                while out == False: #makes it easier to see data by clearing everything and waiting till user wants to move on
                    out = input("Enter any key to escape")
                os.system("cls")

            elif what == '3': #Stats
                out = False
                persent = PercentageCorrect(who)
                for i in range (len(persent)):
                    print(persent[i-1])
                while out == False: #makes it easier to see data by clearing everything and waiting till user wants to move on
                    out = input("Enter any key to escape")
                os.system("cls")
                
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
