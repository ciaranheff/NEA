import random
from Users.AccountManagment import AddSaveData

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
            q = self.Questions[i] #q= question called from the quiz class Questions
            print(q.Question)
            print(q.Choices)
            Ans = input()
            if q.check(Ans) == True:# calls the function to check answer
                print("Correct")
                self.score += 1
            else:
                print("Wrong")
        print("Score was", self.score)
        return(self.score)

######## Questions ############################################
Q1 = MCQuestions("What relative charge does a alpha particle have?",f"1. 0\n2. +1\n3. +2","3")
Q2 = MCQuestions("What is releaed in beta minus decay",f"1. A netral bozon\n2. A negative bozon\n3. A positive boaon","2")
Q3 = MCQuestions("What is not a neuclion?",f"1. A Protron\n2. A Neutron\n3. An Electron","3")
Q4 = MCQuestions("Every Particle has an antiparticle?",f"1. True\n2. False","1")
Q5 = MCQuestions("What is the elctromagnetic force exchange particle?",f"1. Virtual photon\n2. W bozon\n3. Graviton","1")
Q6 = MCQuestions("What is the weak force exchange particle?",f"1. Virtual photon\n2. W bozon\n3. Graviton","2")
Q7 = MCQuestions("What does a kaon decay into?",f"1. Nothing\n2. Electron\n3. Pion","3")
###############################################################

QuestionList = {
    "1": Q1,
    "2": Q2,
    "3": Q3,
    "4": Q4,
    "5": Q5,
    "6": Q6,
    "7": Q7
}

def Adding(Length,QuestionList,quiz):
    quest = []
    questionsToAdd = []
    for i in range (len(QuestionList)): #creates a list of all possible questions
        quest.append(i+1)
    for i in range (Length):
        which = random.randint(0,len(quest)-1) #chooses a random position from the list off remaining possible questions
        what = str(quest[which]) #makes veriable for the name of the question
        questionsToAdd.append(QuestionList[what])#adds the question to the list of questions to from the list of possible questions
        quest.pop(which)# removes the option from the list of remaing questions
    for i in range(Length):
        quiz.NewQuestion(questionsToAdd[i-1])#calls the function to add the questions to the quiz

def QuizStart(QuestionList,UserName):
    quiz = Quiz() #initiates the class in the name quiz
    over = False #loop until over
    while over == False:
        try:
            Length = int(input(f"How many questions would you like 1-{len(QuestionList)}: ")) #lets user choose the length of the quiz
            Adding(Length,QuestionList,quiz)# adds length number of questions to the quiz
            Score = quiz.MultiChoiceStart(Length)# runs the quiz and stores the score
            AddSaveData(UserName,Score,Length) #Saves the data to MultiChoice database
            over = True #breaks loop
        except: # error catches if input is not a int
            print("Enter a number in the range")