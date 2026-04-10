import sqlite3
from Users.LogIn import Hashing
connection = sqlite3.connect('Users.db') # Connects to sql database
cursor = connection.cursor()
    
def Temp():
    cursor.execute("INSERT INTO SaveData VALUES ('1','Temp2','A','Y')")
    cursor.execute("INSERT INTO SaveData VALUES ('2','Temp2','A','Y')")
    cursor.execute("INSERT INTO SaveData VALUES ('3','Temp2','A','N')")
    cursor.execute("INSERT INTO SaveData VALUES ('4','Temp2','A','N')")
    connection.commit()
#################### Users Table ######################

def AddUser(Name,Password,Admin):
    try: # exception handing needed as if Username (because its a PK) already exisits it will cause a crash
        Password = Hashing(Password)
        cursor.execute("INSERT INTO Users (UserName,Password,Admin) VALUES (?,?,?)" , (Name,Password,Admin)) # adds new users
        connection.commit()
        print(f"New user {Name} has been Added")
    except:
        print("*** Error Adding New User ***")

def DeleteUser(Name):
    cursor.execute("DELETE FROM Users WHERE UserName = ?", (Name,)) # deletes user from user databvase
    cursor.execute("DELETE FROM SaveData WHERE UserName = ?", (Name,)) # deletes all user data from savedata database
    cursor.execute("DELETE FROM MultiChoice WHERE UserName = ?", (Name,)) # deletes all user data from MultiChoice database
    connection.commit()


def PasswordChange(Name,NewPassword):
    NewPassword = Hashing(NewPassword)
    cursor.execute("UPDATE Users SET Password = ? WHERE UserName = ?" , (NewPassword,Name,))
    connection.commit()

def AdminChange(Name,NewAdmin):
    cursor.execute("UPDATE Users SET Admin = ? WHERE UserName = ?" , (NewAdmin,Name,))
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
    cursor.execute("SELECT * FROM MultiChoice WHERE UserName = ?", (Name,))
    results += cursor.fetchall()
    return results

def UserQuestion(Name): #need to change quotation marks around as colum names need it when more than 1 word long (in the exacute part)
    cursor.execute('SELECT "Attempt Number" , Correct , "Topic" FROM SaveData WHERE UserName = ?', (Name,))
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

def AddTopicSaveData(UserName,Topic,Correct):
    cursor.execute("INSERT INTO SaveData (UserName,Topic,Correct) VALUES (?,?,?)" , (UserName,Topic,Correct))
    connection.commit()
    
################################# MultiChoice Tables ########################

def UserMultiChoice(Name):
    cursor.execute("SELECT * FROM MultiChoice WHERE UserName = ?", (Name,))
    results = cursor.fetchall()
    return(results)

def MultiChoiceSaveData():
    cursor.execute("SELECT * FROM MultiChoice") # gets all table data from Savedata
    results = cursor.fetchall()
    return results

def AddMultiSaveData(UserName,Score,Total):
    cursor.execute("INSERT INTO MultiChoice (UserName,Score,Total) VALUES (?,?,?)" , (UserName,Score,Total,)) # adds new Savedata
    connection.commit()