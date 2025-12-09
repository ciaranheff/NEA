import sqlite3

connection = sqlite3.connect('Users.db')
cursor = connection.cursor()

def GetUserNames ():
    cursor.execute("SELECT UserName FROM Users") #gets all users from User Database
    results = cursor.fetchall()
    return results

def CheckForUser (Name):
    List = GetUserNames()
    found = False
    for i in range(len(List)): # Compaires given Name with all users in database
        if (Name,) == List[i]:
            found = True
    return(found)

def CheckPassword(Name,Password):
    cursor.execute("SELECT Password FROM Users WHERE UserName = ?" , (Name,)) #gets password from User Database
    results = cursor.fetchall()
    if [Password] == results:
        return True
    else:
        return False
