####################################
# Fortune program, print a random quote on the screen
#


import random

f = file("/usr/share/games/fortunes/fortunes")

fortunes = [] # an array containing all the fortunes
text = "" # accumulator variable, containing one fortune

# run through the file, add lines to current text,
# and add text to fortunes, at separator
for line in f:
    if line == "%\n":
        fortunes.append(text)
        text = ""
    else:
        text = text + line

# print a random fortune
print(random.choice(fortunes))
