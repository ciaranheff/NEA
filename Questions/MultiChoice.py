import random
import json
import os
from Users.AccountManagment import AddMultiSaveData

class MCQuestions:
    def __init__(self,Question,Choices,Answer):#crating OOP stuffs
        self.Question = Question
        self.Choices = Choices
        self.Answer = Answer
    def check(self,AnserGiven):
        if self.Answer == AnserGiven: #checks to see if answer given is correct
            return(True)
        else:
            return(False)

class Quiz:
    def __init__(self): #creating class veriables
        self.Questions = []
        self.score = 0

    def NewQuestion(self,NewQuestion): #function adds new question to question list
        self.Questions.append(NewQuestion)

    def MultiChoiceStart(self,length):
        for i in range (length): 
            q = self.Questions[i] # q= question called from the quiz class Questions
            print(q.Question)
            print(q.Choices)
            Ans = input()
            if q.check(Ans) == True:# calls the function to check answer
                os.system("cls")
                self.score += 1
                print(f"Correct\nScore -",self.score)
            else:
                os.system("cls")
                print(f"Wrong\nScore -",self.score)
        print("Final score was", self.score)
        return(self.score)

######## Questions ############################################
def MakeQuestionList(): #formats the json data correctly and resets list every time new quiz starts
    with open("MultiQuestions.json","r") as f: #opens json file to read from
        data = json.load(f)
    f.close() #closes json file to allow for edditing inother functions
    QuestionList = []
    for i in data["Questions"]:
        options = [i["Option1"] , i["Option2"] , i["Option3"]] #makes each indervidual dictionary value into one veriable to be used in MCQuestions
        Qclass = MCQuestions(i["Question"],options,i["Answer"])# Calls MCQuestions and uses the dictionary value of name veriable options from line above and the answer
        QuestionList.append(Qclass) # Adds the new complete question class to the list of questions that are on the test
    return QuestionList

###############################################################

def Adding(Length,QuestionList,quiz):
    questionsToAdd = []
    for i in range (Length):
        which = random.randint(0,len(QuestionList)-1) #chooses a random position from the list off remaining possible questions
        questionsToAdd.append(QuestionList[which])#adds the question to the list of questions to from the list of possible questions
        QuestionList.pop(which)# removes the option from the list of remaing questions
    for i in range(Length):
        quiz.NewQuestion(questionsToAdd[i-1])#calls the function to add the questions to the quiz

def QuizStart(UserName):
    Length = -1
    QuestionList = MakeQuestionList() # makes list of questions from the json file
    quiz = Quiz() #initiates the class in the name quiz
    over = False #loop until over
    os.system("cls")
    while over == False:
        try:
            while Length < 0:
                Length = int(input(f"How many questions would you like 1-{len(QuestionList)}: ")) #lets user choose the length of the quiz
            Adding(Length,QuestionList,quiz)# adds length number of questions to the quiz
            Score = quiz.MultiChoiceStart(Length)# runs the quiz and stores the score
            AddMultiSaveData(UserName,Score,Length) #Saves the data to MultiChoice database
            over = True #breaks loop
        except: # error catches if input is not a int
            os.system("cls")
            QuestionList = MakeQuestionList()
            print("Enter a number in the range")