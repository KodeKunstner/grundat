#########################################
# AST node type, and parsing functions
##
class Node:
    def __init__(self, type, val, start, end, newline, comment):
        global default_leds, default_nuds, lbps, nuds, leds
        # The type and value of the token,
        # possible types are: number, string, long string, symbol, identifier
        self.type = type
        self.val = val

        # set default led and nud
        self.lbp = 0
        self.led = default_leds[type]
        self.nud = default_nuds[type]

        # set optional leds and nuds
        if type == "symbol" or type == "identifier":
            if lbps.has_key(val):
                self.lbp = lbps[val]
            if nuds.has_key(val):
                self.nud = nuds[val]
            if leds.has_key(val):
                self.led = leds[val]

        # Position of the token in the file
        self.start = start
        self.end = end

        # Indent if token comes right after a newline.
        self.newline = newline

        # Comment text, standing on the line above the token
        self.comment = comment

        # Child nodes, empty by default
        self.children = []

    #################################
    # Utility methods
    ##
    def __repr__(self):
        result = ""
        if self.newline:
            result = result + "\n@" + str(self.start[0]) + ":" + str(self.start[1]) + "\n"
        result = result + self.comment + "token(" + self.type + ", " + str(self.val) + ")"

        result = self.type
        if self.newline:
            result = result + "@" + str(self.start[0]) + ":" + str(self.start[1])
        if not self.comment == "":
            result = result + "C"
        result = result + "('" + self.val + "'"
        for child in self.children:
                result = result + ", " + child.__repr__()
        result = result + ")"
        return result

############################
# Tokeniser
##
src = None
line = 0
pos = 0
buffer = ""
newline = True
comment = ""
start_pos = None

def one_of(str):
    return peek(1) in str

def starts_with(str):
    return peek(len(str)) == str

def ensure_buffer(size):
    global src, buffer
    while len(buffer) < size:
        try:
            buffer = buffer + src.next()
        except StopIteration, exception:
            buffer = buffer + '\0'


def peek(n = 1, pos = 0):
    global buffer
    ensure_buffer(n+pos)
    return buffer[pos:pos+n]

def pop(n = 1):
    global buffer, pos, line
    result = peek(n)
    if result[0] == '\0':
        raise StopIteration
    buffer = buffer[n:]

    # keep track of position in stream
    for c in result:
        pos = pos + 1
        if c == '\n':
            pos = 0
            line = line + 1
    return result

def begin_token():
    global line, pos, start_pos
    start_pos = [line, pos]

def new_token(type, val):
    global src, line, pos, buffer, newline, comment, start_pos
    token = Node(type, val, start_pos, [line, pos], newline, comment)
    newline = False
    comment = ""
    return token

def next():
    """Retrieve the next token"""
    global src, line, pos, buffer, newline, comment, start_pos
   
    # Character set definitions
    whitespace = " \t\r"
    single_symbol = "(){}[].:;,"
    joined_symbol = "=+-*/<>%"
    ident = "_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    digits = "0123456789"
   
    # Repeat the parsing
    while True:
        # Keep track of beginning of token
        begin_token()

        # Skip whitespaces
        if one_of(whitespace):
            pop()

        # Long string
        elif starts_with('"""'):
            s = ""
            pop(3)
            while not starts_with('"""'):
                s = s + pop()
            pop(3)
            return new_token("long string", s)

        # String with escaping
        elif one_of('"\''):
            s = ""
            quote = pop()
            while not starts_with(quote):
                c = pop()
                if c == '\\':
                    c = pop()
                    if c == 'n':
                        c = '\n'
                    elif c == 'r':
                        c = '\r'
                    elif c == 't':
                        c = '\t'
                s = s + c
            c = pop()
            return new_token("string", s)

        # Number
        elif one_of(digits) or (one_of('.-') and peek(1, 1) in digits):
            s = ""
            while one_of('.-' + digits):
                s = s + pop()
            return new_token("number", s)

        # Symbol
        elif one_of(single_symbol):
            return new_token("symbol", pop())
        elif one_of(joined_symbol):
            s = ""
            while one_of(joined_symbol):
                s = s + pop()
            return new_token("symbol", s)

        # Identifier
        elif one_of(ident):
            s = ""
            while one_of(ident + digits):
                s = s + pop()
            return new_token("identifier", s)

        # Newline
        elif peek(1) == "\n":
            pop()
            newline = True

        # Comment
        elif peek(1) == "#":
            s = ""
            pop()
            while not peek() == '\n':
                s = s + pop()
            comment = comment + s + '\n'
            
        # End of file
        elif peek(1) == "\0":
            raise StopIteration

        # Tokenisation error
        else: 
            raise Exception("Unexpected symbol: " + peek(1) + " in line " + line)

######################################
# Parser
##
default_leds = dict()
default_nuds = dict()
lbps = dict()
nuds = dict()
leds = dict()

def invalid(node, left = None):
    raise Exception("Parse error at line " + str(node.start[0]) + ": Unexpected '" + node.val + "'")

def nud_identity(node):
    return node

default_leds["number"] = invalid
default_leds["string"] = invalid
default_leds["long string"] = invalid
default_leds["symbol"] = invalid
default_leds["identifier"] = invalid

default_nuds["number"] = nud_identity
default_nuds["string"] = nud_identity
default_nuds["long string"] = nud_identity
default_nuds["symbol"] = nud_identity
default_nuds["identifier"] = nud_identity

def infix(id, bp = 0):
    global leds, lbps
    def led(node, left):
        node.children = [left, parse(bp)]
        return node
    leds[id] = led


def init_parser(str):
    global src, token
    src = iter(str)
    token = next()

def parse(bp=0):
    global token
    t = token
    token = next()
    left = t.nud(t)
    while bp < token.lbp:
        t = token
        token = next()
        left = t.led(t)
    return left


if __name__ == "__main__":
    init_parser(file("mopy.py").read())
    try:
        while True:
            temp = parse()
            print(temp)
    except StopIteration, exception:
        pass


