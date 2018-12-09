def strip_pun (string):
    punc = '''!()-[]{};:"\<>./?@#$%^&*_~1234567890'''
    no_punc = ""

    for char in string:
        if char not in punc:
            no_punc += char

    return no_punc

def read (txt):
    f= open(txt, "r")
    contents = f.read()
    f.close()
    contents = contents.lower()
    contents = strip_pun(contents)
    contents = contents.split()
    
    return contents
