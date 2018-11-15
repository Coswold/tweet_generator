from sample import Sampling
from markov_chain import markov

def build_string (length, start_word, txt):
    sentence = start_word
    i = 0
    previous_word = start_word
    while i < length:
        hist = markov(txt, previous_word)
        sample = Sampling(hist)
        sample.get_cume()
        previous_word = sample.sample()
        sentence += " " + previous_word
        i += 1

    return sentence
        
