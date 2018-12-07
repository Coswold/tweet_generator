from sample import Sampling
from markov_chain import markov

def build_string (length, window, txt):
    first_word = window.items()
    sentence = first_word[len(first_word) - 1]
    i = 0
    while i < length - 1:
        hist = markov(txt, window)
        sample = Sampling(hist)
        sample.get_cume()
        previous_word = sample.sample()
        sentence += " " + previous_word
        window.enqueue(previous_word)
        window.dequeue()
        i += 1

    return sentence   
