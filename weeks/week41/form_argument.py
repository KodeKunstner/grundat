import cgi, cgitb
cgitb.enable()

print("Content-type: text/html\n")

header = """<html><head><title>Example</title></head><body>"""
footer = """</body>"""

htmlform = """<form action="form_argument.py" method="get">
        <input type="radio" name="vote" value="yes" /> Yes it is!<br />
        <input type="radio" name="vote" value="no" /> No it isn't! <br />
        <input type="submit />
    </form>"""

form = cgi.FieldStorage()

#default page
if not form.has_key("vote"):
    print header + "Is this a form of argument?" + htmlform + footer
elif form["vote"].value == "yes":
    print header + "No it isn't!" + htmlform + footer
elif form["vote"].value == "no":
    print header + "Yes it is!" + htmlform + footer

