import sqlite3

connection = sqlite3.connect('Users.db')
cursor = connection.cursor()

def Hashing(password):
    constant = 0.7321
    final = 0
    length = len(password)
    for i in range(length):
        temp = ord(password[i-1]) * i #changes characters into their unicode value and multiplys it by its weight
        final += temp
    final = round((final * constant),10) # truncates the number
    return(final)

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
    PasswordCheck = Hashing(Password) # hashed password needed to be checked against
    Password = Hashing(Password)
    Password = (Password,) # SQL requests take strings as lists unless stated by a , 
    cursor.execute("SELECT Password FROM Users WHERE UserName = ?" , (Name,)) #gets password from User Database
    results = cursor.fetchone()
    results = float(results[0]) # converts data from sql table into a float for comparison
    if PasswordCheck == results:
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