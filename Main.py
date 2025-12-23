# @@@ = come back to at the end
######### Importing #############
import os
import time
#################################
import Users.LogIn
UL = Users.LogIn
#################################
import Users.AccountManagment
UA = Users.AccountManagment
#################################
import Users.AdminFunctions
UAF = Users.AdminFunctions
#################################
from Questions.Particles import Question1
######### Fuctions #############

################################
def Login(): # Log in for users (lowest level)
    userfound = False
    print(UL.GetUserNames()) #reformat to make look pretty @@@
    while userfound == False:
        User = input("What is your user name ") 
        if UL.CheckForUser(User) == True: #checks to see if user exisits
            userfound = True
        else:
            print("User not found try again")
    PasswordFound = False
    while PasswordFound == False:
        for i in range (3): # 3 attempts before forcing you back to user select
            password = input("What is your password ")
            if UL.CheckPassword(User,password) == True:
                Admin = UL.CheckAdmin(User)
                os.system("cls") # clears screen to prevent clutter
                return (User,Admin)
            else:
                print("wrong password",i+1,"/ 3") #shows number of password attemtps left
        print("Too many wrong attempts")
        time.sleep(1) # gives 1 second to read error message to prevent confusion
        os.system("cls") # clears screen to prevent clutter
        Login() # loops back to the start of the function

def AdminHomeScreen(User):
    while True:
            print("""---Admin Menu---
1. Results Search
2. Manage Users
9. Exit""")
            ans = input()
            if ans == '1':
                os.system("cls")
                UAF.AdminResultsSearch()
            elif ans == '2':
                UAF.AdminAccountManagment()
            elif ans == '9':
                os.system("cls")
                print("Good Bye")
                return()
            else:
                os.system("cls")
                print("invalid input ")

def HomeScreen(User):
    print("User")

######### Veriables #############
User = False
Admin = False
######### Main Loop ##########

while True: 
    if User == False:
        User,Admin = Login()
    else:
        if Admin == True:
            AdminHomeScreen(User)
            break
        else:
            HomeScreen(User)
