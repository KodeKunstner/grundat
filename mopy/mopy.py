class Token:
    def __init__(self, type, val, start, end):
        self.type = type
        self.val = val
        self.start = start
        self.end = end
    def __repr__(self):
        return "token(" + self.type + ", " + str(self.val) + ")"

class TokenStream:
    def __init__(self, src):
        self.src = iter(src)
        self.line = 0
        self.pos = 0
        self.buffer = ""

    def one_of(self, str):
        return self.peek(1) in str

    def starts_with(self, str):
        return self.peek(len(str)) == str

    def ensure_buffer(self, size):
        while len(self.buffer) < size:
            try:
                self.buffer += self.src.next()
            except StopIteration:
                self.buffer += '\0'


    def peek(self, n = 1, pos = 0):
        self.ensure_buffer(n+pos)
        return self.buffer[pos:pos+n]

    def pop(self, n = 1):
        result = self.peek(n)
        if result[0] == '\0':
            raise StopIteration

        # keep track of position in stream
        for c in result:
            self.pos += 1
            if c == '\n':
                self.pos = 0
                self.line += 1
        self.buffer = self.buffer[n:]
        return result

    def begin_token(self):
        self.start_pos = [self.line, self.pos]

    def token(self, type, val):
        return Token(type, val, self.start_pos, [self.line, self.pos])
        return {"type": type,
                "val": val,
                "start": self.start_pos,
                "end": [self.line, self.pos]}
                
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

        # Accumulator string in some cases
        s = ""

        # Skip whitespaces
        while self.one_of(whitespace):
            self.pop()

        # Keep track of beginning of token
        self.begin_token()

        # Long string
        if self.starts_with('"""'):
            self.pop(3)
            while not self.starts_with('"""'):
                s += self.pop()
            self.pop(3)
            return self.token("longstring", s)

        # String with escaping
        elif self.one_of('"\''):
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
                s += c
            c = self.pop()
            return self.token("string", s)

        # Number
        elif self.one_of(digits) or (self.one_of('.-') and self.peek(1, 1) in digits):
            while self.one_of('.-' + digits):
                s += self.pop()
            return self.token("num", s)

        # Symbol
        elif self.one_of(single_symbol):
            return self.token("symb", self.pop())
        elif self.one_of(joined_symbol):
            while self.one_of(joined_symbol):
                s += self.pop()
            return self.token("symb", s)

        # Identifier
        elif self.one_of(ident):
            while self.one_of(ident + digits):
                s += self.pop()
            return self.token("symb", s)

        # Newline
        elif self.peek(1) == "\n":
            self.pop()
            indent = 0
            while self.one_of(whitespace):
                indent += 1
                self.pop()
            return self.token("newline", indent)

        # Comment
        elif self.peek(1) == "#":
            self.pop()
            while not self.peek() == '\n':
                s += self.pop()
            return self.token("comment", s)
            
        # End of file
        elif self.peek(1) == "\0":
            raise StopIteration

        else: 
            raise Exception("Unexpected symbol: " + self.peek(1))


if __name__ == "__main__":
    ts = TokenStream(file("mopy.py").read())
    for token in ts:
        print token

