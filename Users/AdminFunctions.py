########## Importing ############
import os
#################################
import Users.LogIn
UL = Users.LogIn
#################################
import Users.AccountManagment
UA = Users.AccountManagment
#################################

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
                results = (UA.UserAll('temp1')) #retreaves all data raw from database
                for i in range (len(results)): #prints each entry on a new line
                    print(results[i])
                while out == False: #makes it easier to see data by clearing everything and waiting till user wants to move on
                    out = input("Enter any key to escape")
                os.system("cls")
            elif what == '2':# Minmal data
                out = False
                print("Correct Answer - Answer Given - Remake code")
                results = (UA.UserQuestion('temp1')) #retreaves (answer given correct answer and remakecode) from database @@@ change temp1 to 'who'
                for i in range (len(results)): #prints each entry on a new line
                    print(results[i])
                while out == False: #makes it easier to see data by clearing everything and waiting till user wants to move on
                    out = input("Enter any key to escape")
                os.system("cls")
            elif what == '3': #Stats
                pass
            elif what == '9': #Exit
                os.system("cls")
                return()
        else: # catch for when user does not exisit
            print("No user Found")

def PercentageCorrect(who):
    pass