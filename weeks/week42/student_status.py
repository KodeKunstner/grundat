import cgi, cgitb, sqlite3
cgitb.enable()
print("Content-Type: text/html\n")

print "<html><head><title>Godkendte afleveringer</title></head><body>";

fields = cgi.FieldStorage()
db = sqlite3.connect('/home/raj/students.db')

if not fields.has_key("student"):
    print '<form action="student_status.py"><select name="student">'
    cursor = db.cursor()
    result = cursor.execute("SELECT login FROM students")
    for row in result:
        print '<option value="' + row[0] + '">' + row[0] + '</option>'
    print '</select> <input type="submit" value="Vis afleveringer" /></form></html>'

elif fields.getvalue("student") == "all":
    cursor1 = db.cursor()
    cursor2 = db.cursor()
    for student in cursor1.execute("SELECT name,id FROM students"):
        print "" + student [0]+ ": "
        for exercise in cursor2.execute("SELECT exercise FROM handins_passed WHERE student_id=?", (student[1],)):
            print str(exercise[0]) + " "
        print "<br />"

else:
    cursor = db.cursor()
    print fields.getvalue("student") + ": <ul>"
    for exercise in cursor.execute("SELECT exercise FROM handins_passed WHERE student_id IN (SELECT id FROM students WHERE login=?)", (fields.getvalue("student"),)):
        print "<li>Aflevering " + str(exercise[0]) + " ok.</li>";
    print "</ul>"

db.close()
