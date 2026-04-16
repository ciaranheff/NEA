########## Importing ############
import os
import json
import math
########## Functions ##############
from Users.AccountManagment import AddTopicSaveData

class TopicQuestions:
    def __init__(self,Topic,Question,Answer,Number):#crating OOP stuffs
        self.Topic = Topic
        self.Question = Question
        self.Answer = Answer
        self.Number = Number
    def check(self,AnserGiven):
        if self.Answer.lower() == AnserGiven.lower(): #checks to see if answer given is correct
            print("Correct")
            return(True)
        else:
            print("Incorrect")
            return(False)

def MakeQuestionList(): #formats the json data correctly and resets list every time new quiz starts
    Topics = []
    QuestionList = []
    ##### json handling
    with open("TopicQuestions.json","r") as f: #opens json file to read from
        data = json.load(f)
    f.close() #closes json file to allow for edditing inother functions
    #####
    for i in data["Questions"]:
        if (i["Topic"]) not in Topics:#makes a list of all topics by making a list of topics which have already come up and seeing if the current topic value is new or not
            Topics.append(i["Topic"])
        Qclass = TopicQuestions(i["Topic"],i["Question"],i["Answer"],i["Number"])# Calls TopicQuestions and uses the dictionary values from json file
        QuestionList.append(Qclass) # Adds the new complete question class to the list of questions that are on the test
    return QuestionList,Topics

def TopicMenu(User):
    User = User
    QuestionList,Topics = MakeQuestionList()
    while True:
        print(Topics)
        What = input("What topic would you like to do (press enter to exit) - ")
        if What.strip() == "":
            os.system("cls")
            break
        for i in Topics:
            if What.lower().strip() == i.lower(): #compairs the word input with the topic name by making both inputs lower case and removing any empty space with strip
                os.system("cls")
                print("What question would you like to answer? - ")
                for i in QuestionList: # liniar search for items with the topic class of veriable What
                    if What.lower().strip() == i.Topic.lower():
                        print(i.Question,i.Number)
                try: #makes sure user input is a number
                    Quest = int(input("What question Number would you like to do - ")) # gets the user to input the questoin number they want to do
                except:
                    Quest = ""
                    os.system("cls")
                    print("invalid number input")
                for i in QuestionList:
                    if Quest == i.Number and i.Topic == What:
                        Correct = (QuestionChosen(i))
                        AddTopicSaveData(User,i.Topic,Correct)

def QuestionChosen(i):
    print(i.Question)
    ans = (input("")).lower()
    Correct = i.check(ans) #calls the class function check which prints if its correct for the user and returns a boolean output
    return(Correct)