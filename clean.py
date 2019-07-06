def strip_pun (string):
    punc = '''!;.?'''
    no_punc = "[start] "

    for char in string:
        if char not in punc:
            no_punc += char
        else:
            no_punc += ' [stop] [start] '

    no_punc += ' [stop]'
    return no_punc

def read (txt):
    f= open(txt, "r")
    contents = f.read()
    f.close()
    contents = contents.lower()
    contents = strip_pun(contents)
    contents = contents.split()

    return contents
