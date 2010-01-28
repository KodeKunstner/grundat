# -*- coding: utf-8 -*-

import cgi, cgitb, random
import sorting

cgitb.enable()

# Print Content Type
print 'Content-type: text/html; charset=utf-8\n'

# Opbyg et dictionary (ordbog) af HTML forme (en for hvert spørgsmål)
htmlforms = {}

# HTML form for valg af problemtype
htmlforms['problem_type'] = '''
<b>Hvilken type problem skal jeg løse?:</b>
<form action="solver.py" method="POST">
<p>Problemtype:
  <select name="problem_type">
    <option value="sort">Sortering</option>
    <option value="search">Søgning</option>
    <option value="sudoku">Sudoku</option>
  </select></p>
  <input type="submit" value="Indsend"/>
</form>'''

# HTML form for valg af algoritme ved sortering
# Bemærk: Skjult felt viderefører "problem_type"
htmlforms['sort'] = '''
<b>Hvilken algoritme skal jeg bruge?</b>
<form action="solver.py" method="POST">
<p>Algoritme:
  <select name="algorithm">
    <option value="insertion_sort">Insertion Sort</option>
    <option value="bubble_sort">Bubble Sort</option>
    <option value="merge_sort">Merge Sort</option>
    <option value="quick_sort">Quick Sort</option>
    <option value="builtin_sort">Pythons indbyggede sortering</option>
    <option value="all">ALLE!</option>
  </select></p>
<p>Antal elementer:<br/>
  <input type="text" name="problem_size" value="2000" />
</p>
<input type="hidden" name="problem_type" value="sort" />
<input type="submit" value="Sorter!"/>
</form>
'''


# Print HTML header
print '''<html>
<head></head>
<body>'''


# Indlæs form værdier
form = cgi.FieldStorage()
f_type = form.getvalue('problem_type')
f_algo = form.getvalue('algorithm')
f_size = form.getvalue('problem_size')

if not f_type:
    # Print HTML form til valg af problem type
    print htmlforms['problem_type']

elif not f_algo:
    if f_type in htmlforms:
        # Print HTML form til valg af algoritme
        print htmlforms[f_type]
    else:
        print 'Den valgte problemtype er ikke understøttet.'

else:
    if f_type == 'sort':
        # Start HTML tabel
        print '<table><tr><td>Algoritme:</td><td>Tid:</td></tr>'
        for result in sorting.sort(f_algo, int(f_size)):
            # Udpak resultat
            name, time = result
            # Gør navnet lidt pænere
            name = name.replace('_', ' ').title()
            # Print HTML række
            print '<tr><td>%s:</td><td>%.4f</td></tr>' % (name, time)
        # Slut HTML tabel
        print '</table>'

# Print HTML footer
print '''</body></html>'''
