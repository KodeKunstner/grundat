# -*- coding: utf-8 -*-
# The line above is needed to have international characters, æøå
# This file is a short example of how you could generate simple form letters

names = ["Annette", "Boris", "Constantin", "Dorthea", "Eigil", "Frederikke"]

letter = """
Kære NAVN,

det ville glæde mig
at se dig til gilde
d. 20/10 2010,

mange hilsner
   Gertrud
"""

for name in names:
    print(letter.replace("NAVN", name))
