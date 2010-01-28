print 'Content-type: text/html\n'

html_form = """
<html><body>
<form method="get" action="strings.py">
Navn: <input name="navn"/>   <br/>
Email: <input name="email"/> <br/>
<input type="submit" />
</form>"""

html_ok = """
<html><body>
Du er blevet oprettet!
Dit navn er %(navn)s ;-)
</html></body>"""

html_fejl = """
<html><body>
Der er sket en fejl: %(fejl)s <br/>
Udfyld venligst formen igen:
<a href="strings.py">Klik her</a>
"""

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
navn  = form.getvalue('navn')
email = form.getvalue('email')

if navn != None or email != None:
    if navn == None:
        print html_fejl % {'fejl': 'Du har ikke angivet et navn!'}
    elif email == None:
        print html_fejl % {'fejl': 'Du har ikke angivet en email!'}
    else:
        # Put ting i databasen ...
        print html_ok % {'navn': navn}
else:
    print html_form
