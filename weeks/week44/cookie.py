import Cookie, os


# Funktioner til haandtering af cookies
def cookie_load():
    global _COOKIES
    _COOKIES = Cookie.SmartCookie()
    _COOKIES.load(os.environ.get('HTTP_COOKIE',''))

def cookie_get(name):
    if name in _COOKIES:
        return _COOKIES[name].value
    return None

def cookie_set(name, value):
    _COOKIES[name] = value
    _COOKIES[name]['version'] = 1
    _COOKIES[name]['max-age'] = 3600

def cookie_send_headers():
    print _COOKIES



# Indlaes cookies fra forespoergsel
cookie_load()

# Hent cookie'en "count" (vores taeller)
count = cookie_get('count')

# Hvis taelleren ikke var sat: saet den til 0
if count == None:
    count = 0

# Tael en op
count += 1

# Gem den nye vaerdi
cookie_set('count', count)

# Send cookie-headeren til browseren (inden vi printer "Content-type")
cookie_send_headers()

# Content-type
print 'Content-type: text/html; charset: utf-8\n'

# Soed besked
print 'Du har besoegt siden %s gange.' % count
