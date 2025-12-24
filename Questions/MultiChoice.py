class MCQuestions:
    def __init__(self,Question,Choices,Answer):
        self.Question = Question
        self.Choices = Choices
        self.Answer = Answer
    def check(self,AnserGiven):
        if self.Answer == AnserGiven:
            return(True)
        else:
            return(False)

class Quiz:
    def __init__(self):
        self.Questions = []
        self.score = 0

    def NewQuestion(self,NewQuestion):
        self.Questions.append(NewQuestion)

    def MultiChoiceStart(self):
        for i in range (3):
            q = self.Questions[i]
            print(q.Question)
            print(q.Choices)
            Ans = input()
            if q.check(Ans) == True:
                print("Correct")
                self.score += 1
            else:
                print("Wrong")
        print("Score was", self.score)


######## Questions ############################################
Q1 = MCQuestions("What relative charge does a alpha particle have?",f"1. 0\n2. +1\n3. +2","3")
Q2 = MCQuestions("What is releaed in beta minus decay",f"1. A netral bozon\n2. A negative bozon\n3. A positive boaon","2")
Q3 = MCQuestions("What is not a neuclion?",f"1. A Protron\n2. A Neutron\n3. An Electron","3")
###############################################################

#add questions to dictionary
#randomly choose x number of questions
#put into a stack to randomise order
#do quiz.NewQuestions on them
#do quiz


quiz = Quiz()
quiz.NewQuestion(Q1)
quiz.NewQuestion(Q2)
quiz.NewQuestion(Q3)

quiz.MultiChoiceStart()

