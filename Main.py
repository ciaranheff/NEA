######### Importing #############
import Users.LogIn
UL = Users.LogIn
#################################
import Users.AccountManagment
UA = Users.AccountManagment
#################################
from Questions.Particles import Question1
######### Fuctions #############

def Login(): # Log in for users (lowest level)
    userfound = False
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
                return (User,Admin)
                break # breaks out of the loop preventing any unessisary loops
            else:
                print("wrong password",i+1,"/ 3") #shows number of password attemtps left
        print("Too many wrong attempts")
        print("##############") # replace with cls
        Login()

def HomeScreen(User):
    print("here")


######### Veriables #############
User = False
Admin = False
######### Main Loop ##########
while True: 
    if User == False:
        User,Admin = Login()
        print(User,Admin)
    else:
        HomeScreen(User)
        break