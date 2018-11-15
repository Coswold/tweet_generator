from dictogram import Dictogram

def markov (txt):
    m_chain = {}
    for word in txt[:-1]:
        if word not in m_chain:
            i = 0
            new = []
            while i < len(txt) - 1:
                if txt[i] == word:
                    new.append(txt[i + 1])
                i += 1
            m_chain[word] = Dictogram(new)
    return m_chain
