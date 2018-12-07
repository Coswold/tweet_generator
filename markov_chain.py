from dictogram import Dictogram   

def markov (txt, window):
    hist = []
    new = []
    i = 0
    words = window.items()
    print(words)
    while i < len(txt) - 1:
        j = len(words) - 1
        if txt[i] == words[len(words) - 1]:
            k = i
            while j > 0:
                if txt[k] == words[j]:
                    j -= 1
                    k -= 1
                else:
                    break
            if j == 0:
                new.append(txt[i + 1])
                print(new)
        i += 1
    hist = Dictogram(new)
    return hist
