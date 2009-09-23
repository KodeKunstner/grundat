# -*- coding: utf-8 -*-
import random

def guess_a_number(n):
    number = random.randint(1, n)
    guess = requestInteger("Gæt et tal mellem 1 og " + str(n))

    while not guess == number:
        if guess < number:
            guess = requestInteger("For lille, gæt igen")
        else:
            guess = requestInteger("For stort, gæt igen")
            
    print("Tillyke, du gættede det")
