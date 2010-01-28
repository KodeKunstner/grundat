import cgi, cgitb
cgitb.enable()
print("Content-Type: text/html\n")

import sqlite3

def create_table():
    fields = cgi.FieldStorage()
    for name in fields:
        print(name + ": " + fields[name].value + "<br />")
    
    db = sqlite3.connect('students.db')
    cursor = db.cursor()
    
    cursor.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name VARCHAR(255), login VARCHAR(255), email VARCHAR(255));")
    for person in read_data("/home/rasmusjensen/login_mail/navne_liste"):
        cursor.execute("INSERT INTO STUDENTS (name, login, email) VALUES (?, ?, ?);", person)

    cursor.execute("CREATE TABLE handins_passed (student_id INTEGER, exercise INTEGER);")

    db.commit()
    db.close()
    
    

def da_to_en(str):
    return str.replace(
        '\xc3\xa6', 'ae').replace(
        '\xc3\x86', 'AE').replace(
        '\xc3\xb8', 'o').replace(
        '\xc3\x98', 'O').replace(
        '\xc3\xa5', 'aa').replace(
        '\xc3\x85', 'Aa')

def read_data(filename):
    names = []
    for line in file(filename):
        line = line.split(":")
        navn = line[0].strip()
        email = line[1].strip()
        brugernavn = da_to_en(navn).lower().replace(" ", "").replace("-","")
        names.append((da_to_en(navn.split()[0]), brugernavn, email))
    return names

create_table()
