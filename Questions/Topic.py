########## Importing ############
import os
#################################
import json
#################################
import math

class TopicQuestions:
    def __init__(self,Topic,Question,Answer):#crating OOP stuffs
        self.Topic = Topic
        self.Question = Question
        self.Answer = Answer
    def check(self,AnserGiven):
        if self.Answer == AnserGiven: #checks to see if answer given is correct
            return(True)
        else:
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
        Qclass = TopicQuestions(i["Topic"],i["Question"],i["Answer"])# Calls TopicQuestions and uses the dictionary values from json file
        QuestionList.append(Qclass) # Adds the new complete question class to the list of questions that are on the test
    return QuestionList,Topics

def TopicMenu(User):
    QuestionList,Topics = MakeQuestionList()
    print(Topics)
    while True:
       What = input("What topic would you like to do- ") #change to make not case sensative