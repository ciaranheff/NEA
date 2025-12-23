import sqlite3
connection = sqlite3.connect('Users.db') # Connects to sql database
cursor = connection.cursor()

def Temp():
    cursor.execute("INSERT INTO SaveData VALUES ('4','temp4','A','ABC','15','Y')")
    connection.commit()
    

#################### Users Table ######################

def AddUser(Name,Password,Admin):
    try: # exception handing needed as if Username (because its a PK) already exisits it will cause a crash
        cursor.execute("INSERT INTO Users (UserName,Password,Admin) VALUES (?,?,?)" , (Name,Password,Admin)) # adds new users
        connection.commit()
        print(f"New user {Name} has been Added")
    except:
        print("*** Error Adding New User ***")

def DeleteUser(Name):
    cursor.execute("DELETE FROM Users WHERE UserName = ?", (Name,)) # deletes user from user databvase
    cursor.execute("DELETE FROM SaveData WHERE UserName = ?", (Name,)) # deletes all user data from savedata database
    connection.commit()


def PasswordChange(Name,NewPassword):
    cursor.execute("UPDATE Users SET Password = ? WHERE UserName = ?" , (NewPassword,Name,))
    connection.commit()

def AdminChange(Name,NewAdmin):
    cursor.execute("UPDATE Users SET Password = ? WHERE UserName = ?" , (NewAdmin,Name,))
    connection.commit()

def ShowAll(): #Admin perammeter needed as it will show passwords
    cursor.execute("SELECT * FROM Users")
    results = cursor.fetchall()
    return results

#print(ShowAll("Y")) shows all SQL database for users DEBUG USE ONLY

######################### SaveData Table #######################

def SaveData():
    cursor.execute("SELECT * FROM SaveData") # gets all table data from Savedata
    results = cursor.fetchall()
    return results

def UserAll(Name): # gets all user specific from Savedata
    cursor.execute("SELECT * FROM SaveData WHERE UserName = ?", (Name,))
    results = cursor.fetchall()
    return results

def UserQuestion(Name): #need to change quotation marks around as colum names need it when more than 1 word long (in the exacute part)
    cursor.execute('SELECT Correct , "Answer Give" , "Remake Code" FROM SaveData WHERE UserName = ?', (Name,))
    results = cursor.fetchall()
    return results

def UserCorrectAll(Name):
    cursor.execute("SELECT Correct FROM SaveData WHERE UserName = ?", (Name,))
    results = cursor.fetchall()
    return results

def UserCorrectSubject(Name,Subject):
    cursor.execute("SELECT Correct FROM SaveData WHERE UserName = ? AND Topic = ?", (Name,Subject,))
    results = cursor.fetchall()
    return results

def CorrectSubject(Subject):
    cursor.execute("SELECT * FROM SaveData WHERE Topic = ?" ,(Subject,))
    results = cursor.fetchall()
    return results