questions = [ 
    ["Hvad er Python?", 
      ["et programmeringssprog", "en slange", "en komedietrup"], 
      [True, True, True]],
    ["Hvad er strenge, lister, dictionaries?", 
      ["sammensatte datatyper", "dele af musikinstrumenter", "variable"], 
      [True, False, False]],
    ["Hvad staar r'...' for i forbindelse med en streng?", 
      ["raw, - teksten er praecist som den staar", "reverse - bogstaverne kommer i omvendt raekkefaelge"], 
      [True, False]]
    ]

# counter variable for the number of correct answers
correct = 0

# run through the questions, asking them one by one
for question in questions:
    question_string = question[0]
    answers = question[1]
    truthvalue = question[2]
    for answer_number in range(len(answers)):
        question_string = question_string + "\n" + str(answer_number) + ") " + answers[answer_number]
    guess = requestIntegerInRange(question_string, 0, len(answers)-1)
    printNow(answers)
    if truthvalue[guess]:
        correct = correct + 1

showInformation("Correct = " + str(correct) + " / " + str(len(questions)))
