import sqlite3
connection = sqlite3.connect('Users.db')
cursor = connection.cursor()

table1 = """CREATE TABLE IF NOT EXISTS MultiChoice (
    "Attempt Number" INTEGER PRIMARY KEY,
    UserName TEXT,
    Score INTEGER,
    Total INTEGER
)"""

table2 = """CREATE TABLE IF NOT EXISTS "SaveData" (
	"Attempt Number"	INTEGER,
	"UserName"	TEXT,
	"Topic"	TEXT,
	"Correct"	INTEGER,
	PRIMARY KEY("Attempt Number"),
	FOREIGN KEY("UserName") REFERENCES "Users"("UserName")
)"""

table3 = """CREATE TABLE IF NOT EXISTS "Users" (
	"UserName"	TEXT,
	"Password"	TEXT,
	"Admin"	TEXT,
	PRIMARY KEY("UserName")
)"""