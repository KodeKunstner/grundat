def translate(string):
    """Make a direct translation, by replacing english words with danish words"""

    # set of words used in the translation
    dict = {
        "a": "en",
        "another": "endnu",
        "hello": "hej",
        "is": "er",
        "is": "er",
        "next": "naeste",
        "now": "nu",
        "test": "test",
        "this": "dette",
        "what": "hvad",
        "world": "verden" }
    
    # run through the words in the string, 
    # and replace with known words
    result = ""
    for word in string.split():
        if dict.has_key(word):
            result = result + dict[word]
        else:
            result = result = word
        result = result + " "
    return result

# Try to run som simple direct translations
print(translate("hello world"))
print(translate("now this is a test"))
print(translate("what is next"))
print(translate("another a test"))

