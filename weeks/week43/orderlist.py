# -*- coding: utf-8 -*-


## Start of CGI script
import cgitb, cgi, sys
cgitb.enable()

print 'Content-type: text/html; charset=utf-8\n'


# Open order database
import sqlite3
db = sqlite3.connect('data/shop.db')
cursor = db.cursor()

# Fetch orders
cursor.execute("SELECT * FROM orders")
orders = cursor.fetchall()
cursor.close()

# Print HTML header
print """
<html><body>
<h1>Liste over ordre</h1>"""

# Print table header
print """
<table>
<tr><td>Navn</td><td>Email</td><td>Pris</td><td>Produkter</td></tr>
"""

# Print table row for each order
for order in orders:
    print '<tr>'
    id, name, email, products, price = order
    print '<td>', name, '</td><td>', email, '</td><td>', price, '</td><td>', products, '</td>'
    print '</tr>'

# Print table footer
print "</table>"

# Print HTML footer
print "</body></html>"
