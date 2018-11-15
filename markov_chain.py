from dictogram import Dictogram

def markov (txt, word):
    hist = []
    new = []
    i = txt.index(word)
    while i < len(txt) - 1:
        if txt[i] == word:
            new.append(txt[i + 1])
        i += 1
    hist = Dictogram(new)
    return hist
