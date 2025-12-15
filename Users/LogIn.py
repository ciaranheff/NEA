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
    Password = (Password,) # SQL requests take strings as lists unless stated by a , 
    cursor.execute("SELECT Password FROM Users WHERE UserName = ?" , (Name,)) #gets password from User Database
    results = cursor.fetchall()
    if [Password] == results:
        return True
    else:
        return False
    
def CheckAdmin(Name):
    cursor.execute("SELECT Admin FROM Users WHERE UserName = ?" , (Name,)) #gets admin status from User Database
    results = cursor.fetchall()
    if [('Y',)] == results: # checks to see if admin status is true
        return True
    else:
        return False