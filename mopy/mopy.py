############################
# Tokeniser
##
class TokenStream:
    def __init__(self, src):
        self.src = iter(src)
        self.line = 0
        self.pos = 0
        self.buffer = ""
        self.newline = True
        self.comment = ""

    def one_of(self, str):
        return self.peek(1) in str

    def starts_with(self, str):
        return self.peek(len(str)) == str

    def ensure_buffer(self, size):
        while len(self.buffer) < size:
            try:
                self.buffer = self.buffer + self.src.next()
            except StopIteration, exception:
                self.buffer = self.buffer + '\0'


    def peek(self, n = 1, pos = 0):
        self.ensure_buffer(n+pos)
        return self.buffer[pos:pos+n]

    def pop(self, n = 1):
        result = self.peek(n)
        if result[0] == '\0':
            raise StopIteration
        self.buffer = self.buffer[n:]

        # keep track of position in stream
        for c in result:
            self.pos = self.pos + 1
            if c == '\n':
                self.pos = 0
                self.line = self.pos + 1
        return result

    def begin_token(self):
        self.start_pos = [self.line, self.pos]

    def token(self, type, val):
        token = Node(type, val, self.start_pos, [self.line, self.pos], self.newline, self.comment)
        self.newline = False
        self.comment = ""
        return token

    def __iter__(self):
        """Needed to make the object iterable"""
        return self

    def next(self):
        """Retrieve the next token"""
   
        # Character set definitions
        whitespace = " \t\r"
        single_symbol = "(){}[].:;,"
        joined_symbol = "=+-*/<>%"
        ident = "_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        digits = "0123456789"
   
        # Repeat the parsing
        while True:
            # Keep track of beginning of token
            self.begin_token()
    
            # Skip whitespaces
            if self.one_of(whitespace):
                self.pop()
    
            # Long string
            elif self.starts_with('"""'):
                s = ""
                self.pop(3)
                while not self.starts_with('"""'):
                    s = s + self.pop()
                self.pop(3)
                return self.token("long string", s)
    
            # String with escaping
            elif self.one_of('"\''):
                s = ""
                quote = self.pop()
                while not self.starts_with(quote):
                    c = self.pop()
                    if c == '\\':
                        c = self.pop()
                        if c == 'n':
                            c = '\n'
                        elif c == 'r':
                            c = '\r'
                        elif c == 't':
                            c = '\t'
                    s = s + c
                c = self.pop()
                return self.token("string", s)
    
            # Number
            elif self.one_of(digits) or (self.one_of('.-') and self.peek(1, 1) in digits):
                s = ""
                while self.one_of('.-' + digits):
                    s = s + self.pop()
                return self.token("number", s)
    
            # Symbol
            elif self.one_of(single_symbol):
                return self.token("symbol", self.pop())
            elif self.one_of(joined_symbol):
                s = ""
                while self.one_of(joined_symbol):
                    s = s + self.pop()
                return self.token("symbol", s)
    
            # Identifier
            elif self.one_of(ident):
                s = ""
                while self.one_of(ident + digits):
                    s = s + self.pop()
                return self.token("identifier", s)
    
            # Newline
            elif self.peek(1) == "\n":
                self.pop()
                self.newline = True
    
            # Comment
            elif self.peek(1) == "#":
                s = ""
                self.pop()
                while not self.peek() == '\n':
                    s = s + self.pop()
                self.comment = self.comment + s + '\n'
                
            # End of file
            elif self.peek(1) == "\0":
                raise StopIteration

            # Tokenisation error
            else: 
                raise Exception("Unexpected symbol: " + self.peek(1) + " in line " + self.line)

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

    ##################################
    # Left Denominators
    ##

    def led_invalid(self, left):
        raise Exception('Invalid led "' + self.val + '" at line: ' + str(self.start[0]))

    #################################
    # Null Denominators
    ##
    def nud_id(self):
        return self

    def nud_invalid(self):
        raise Exception('Invalid nud "' + self.val + '" at line: ' + str(self.start[0]))

    #################################
    # Utility methods
    ##
    def __repr__(self):
        result = ""
        if self.newline:
            result = result + "\n@" + str(self.start[0]) + ":" + str(self.start[1]) + "\n"
        result = result + self.comment + "token(" + self.type + ", " + str(self.val) + ")"
        return result

#################################
# Parser
##
default_nuds = dict()
default_leds = dict()
lbps = dict()
nuds = dict()
leds = dict()

# Default null denominators
default_nuds["number"] = Node.nud_id
default_nuds["string"] = Node.nud_id
default_nuds["long string"] = Node.nud_id
default_nuds["symbol"] = Node.nud_invalid
default_nuds["identifier"] = Node.nud_id

# Default left denominators
default_leds["number"] = Node.led_invalid
default_leds["string"] = Node.led_invalid
default_leds["long string"] = Node.led_invalid
default_leds["symbol"] = Node.led_invalid
default_leds["identifier"] = Node.led_invalid

def init_parser(src):
    token_stream = TokenStream(src)
    next_token()

def next_token():
    global token
    token = token_stream.next()
    return token

def parse(bp=0):
    global token
    t = token
    next_token()
    left = t.nud()
    while bp < token.lbp:
        t = token
        next_token()
        left = t.led(left)
    return left


if __name__ == "__main__":
    ts = TokenStream(file("mopy.py").read())
    try:
        while True:
            token = ts.next()
            print(token)
    except StopIteration, exception:
        pass


