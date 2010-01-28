import cgi, cgitb
cgitb.enable()
print("Content-Type: text/html\n")

fields = cgi.FieldStorage()
for name in fields:
    print(name + ": " + fields[name].value + "<br />")

