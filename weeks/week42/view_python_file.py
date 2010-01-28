# The reason this file was created is not as an example,
# but as a way to show the python code examples.
# - the web server executes them by default, and does
# thus not show the source code...
#
# This also works fine as an example of a practical script
import sys, cgi, re, cgitb
cgitb.enable()

form = cgi.FieldStorage()
filename = form.getvalue("filename")

print """Content-Type: text/html

<html><head><title>Python fil</title></head>
<body>
"""
print '<p><a href="../%s">%s</a></p><pre>' % (filename,filename)
# You may ignore the re.compi.... part
# (This test if the filename is within the example directories
# as a safety measure -- otherwise the script could be used
# to read arbitrary files on the server)
if not re.compile("^u[0-9][0-9]/[a-zA-Z0-9_]*.py$").match(filename):
    print "Error: filename is not valid"
else:

    # load the file and show it
    print file("../" + filename).read().replace("<", "&lt;");
print "</pre></body>"
