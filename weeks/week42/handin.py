#!/usr/bin/env python 
import sys, sqlite3

if len(sys.argv) < 3:
    print "Usage: handin.py studentlogin exercisenumber [passed | nonpassed | ]"
    sys.exit(1)

login = sys.argv[1]
exercise = int(sys.argv[2])
passed = (len(sys.argv) == 3) or sys.argv[3] == "passed"

db = sqlite3.connect('/home/raj/students.db')
c = db.cursor()
if passed:
    c.execute("INSERT INTO handins_passed (student_id, exercise) SELECT id, ? FROM students WHERE login=?", (exercise, login))
else:
    c.execute("DELETE FROM handins_passed WHERE exercise=? AND student_id IN (SELECT id FROM students WHERE login=?)", (exercise, login))

db.commit()
