# User1 password = 1234 
# User2 password = 22222
# User3 password = 333
# Admin password = pppp
######### Importing ##############
import os
import time
#################################
import Users.LogIn
UL = Users.LogIn
#################################
import Users.AdminFunctions
UAF = Users.AdminFunctions
#################################
from Questions.MultiChoice import QuizStart
#################################
from Questions.Topic import TopicMenu
################################
from Users.AdminFunctions import GetTopics

def Login(): # Log in for users (lowest level)
    userfound = False
    names = (UL.GetUserNames()) 
    for i in names:
        print(i[0])
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
                #os.system("cls") # clears screen to prevent clutter
                return (User,Admin)
            else:
                print("wrong password",i+1,"/ 3") #shows number of password attemtps left
        print("Too many wrong attempts")
        time.sleep(1) # gives 1 second to read error message to prevent confusion
        os.system("cls") # clears screen to prevent clutter
        return Login() # loops back to the start of the function

#######################################################

def AdminHomeScreen(User): # For admins
    os.system("cls")
    while True:
        ans = input(f"---Admin Menu---\n1. Results Search\n2. Manage Users\n3. Question Edditing\n9. Exit\n")
        if ans == '1':
            os.system("cls")
            UAF.AdminResultsSearch()
        elif ans == '2':
            UAF.AdminAccountManagment()
        elif ans == '3':
            UAF.EdditingQuestionsMenus()
        elif ans == '5':
            os.system("cls")
            UAF.PercentageCorrect('User1')
        elif ans == '9':
            os.system("cls")
            print("Good Bye")
            return()
        else:
            os.system("cls")
            print("invalid input ")

def HomeScreen(User): # For Users
    os.system("cls")
    while True:
        ans = input(f"---Main Menu---\n1.Topic selection\n2.Multichoice\n3.Ranks\n9.Exit\n")
        if ans == "1":
            os.system("cls")
            TopicMenu(User)
        elif ans == "2":
            os.system("cls")
            QuizStart(User)
        elif ans == "3":
            os.system("cls")
            Rankings()
        elif ans == "9":
            os.system("cls")
            print("Good Bye")
            return()
        else:
            os.system("cls")
            print("invalid input")

###########################################################################

def DisplayRank(rank,topic):
    print(f"{topic} Rankings:")
    for i in range (len(rank)):
        print(f"{i+1}. {rank[i][0]} - {rank[i][1]}%")

def Sorting(topic): # Sorting algorythm to order the list highest to lowest
    temp = []
    n = len(topic)
    for i in range(n):
        for j in range(0, n-i-1):
            if topic[j][1] < topic[j+1][1]: # if lower value is less than higher value swap
                temp = topic[j] #temp used to store value before it is changed 
                topic[j] = topic[j+1]
                topic[j+1] = temp
    return(topic)

def Rankings():
    allscores = []
    topics = GetTopics()
    topics.append("Total") # adds the catagory total to list of topics as would otherwise be skipped over
    names = (UL.GetUserNames())
    for i in names:
        scores = UAF.PercentageCorrect(i[0]) # retreves the score of each user and adds them into a 3D list
        allscores.append([scores , i[0]]) # 3D array
    for topic in topics: # for every topic in the list
        rank = []
        for i in allscores:# splits list enteries into distinct veriables
            stats = i[0]
            username = i[1]
            for j in stats:
                subject = j[0]
                score = j[1]
                if subject == topic and score != 'NA': #removes any entery where the score is kept as NA as sorting algorythm can only sort numbers
                    rank.append([username,score])
        rank = Sorting(rank)
        DisplayRank(rank,topic)
    UAF.KeepIn()

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
            break