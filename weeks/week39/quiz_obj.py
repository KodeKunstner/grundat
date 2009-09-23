# -*- coding: utf-8 -*-
import random

class MultProblem(object):
    def __init__(self):
        self.a = random.randint(1, 10)
        self.b = random.randint(1, 10)

    def question(self):
        return "Hvad er " + str(self.a) + " * " + str(self.b) + "?"

    def answer_ok(self, answer):
        return int(answer) == self.a * self.b


class QuizProblem(object):
    def __init__(self, question, answer):
        self.quest = question
        self.answer = answer.strip().lower()

    def question(self):
        return self.quest


    def answer_ok(self, answer):
        return str(answer).strip().lower() == self.answer

def quiz(problems):
    for problem in problems:
        print problem.question()
        if problem.answer_ok(raw_input()):
            print("Rigtigt!")
        else:
            print("Forkert!")


problems = []
problems.append(QuizProblem("Hvad er Danmarks østligste ø?", "Christiansø"))
problems.append(QuizProblem("Hvor mange primtal er mindre end 10?", "4"))
problems.append(MultProblem())
problems.append(MultProblem())
problems.append(MultProblem())
random.shuffle(problems)
quiz(problems)

