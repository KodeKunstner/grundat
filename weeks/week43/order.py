# -*- coding: utf-8 -*-


## Start of CGI script
import cgitb, cgi, sys
cgitb.enable()

print 'Content-type: text/html; charset=utf-8\n'


def error(s):
    """ print error message and exit """
    print s
    sys.exit()


# List of products and their prices
products = {'hat': 290, 'shirt': 480, 'pants': 520, 'shoes': 340, 'socks': 110}


# Get form fields
fields = cgi.FieldStorage()


# Get user information
name  = fields.getvalue('name')
email = fields.getvalue('email')

# Verify information
if name == None or len(name) < 2:
    error('Du skal indtaste et navn!')
elif email == None or not '@' in email:
    error('Email-addressen er noget vås!')



# Compute total price of order
total_price = 0
products_chosen = []
for product in products:
    if product in fields:
        total_price += products[product]
        products_chosen.append(product)

# Check if any products were selected
if len(products_chosen) == 0:
    error('Du har ikke valgt noget produkt!')



# Open order database
import sqlite3
db = sqlite3.connect('data/shop.db')
cursor = db.cursor()

cursor.execute("INSERT INTO orders (name, email, product_list, price) VALUES (?, ?, ?, ?)",
               (name, email, str(products_chosen), total_price))
db.commit()
cursor.close()

# All well
print 'Din ordre er blevet gennemført!'

