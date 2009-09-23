import random

class QuizAddProblem(object):
    
    def __init__(self):
        self.tal1 = random.randint(1,100)
        self.tal2 = random.randint(1,100)

    def sporgsmaal(self):
        return "Hvad er " + str(self.tal1) + " + " + str(self.tal2) + "?"
    
    def svar_rigtigt(self, svar):
        if int(svar) == self.tal1 + self.tal2:
            return True
        else:
            return False

class QuizMultProblem(object):
    def __init__(self):
        self.tal1 = random.randint(1,20)
        self.tal2 = random.randint(1,20)

    def sporgsmaal(self):
        return "Hvad er " + str(self.tal1) + " * " + str(self.tal2) + "?"
    
    def svar_rigtigt(self, svar):
        if int(svar) == self.tal1 * self.tal2:
            return True
        else:
            return False


def quiz(problemlist):
    for problem in problemlist:
        print problem.sporgsmaal()
        svar = raw_input()
        if problem.svar_rigtigt(svar):
            print "Rigtigt!"
        else:
            print "Forkert!"
            


problems = []
for x in range(5):
    problems.append(QuizAddProblem())
problems.append(QuizMultProblem())
random.shuffle(problems)
#quiz(problems)

class eksempel(object):
    bar = "432"
    def __init__(self):
        self.foo = "123"
    def f(self):
        print "hello"
        



