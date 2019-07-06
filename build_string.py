from sample import Sampling
from markov_chain import Markov
from queue1 import Queue1
from clean import read

def build_string (txt):
    window = Queue1()
    m = Markov(txt)
    start = m.get_start()
    window.enqueue(start[0])
    window.enqueue(start[1])
    sentence = ""
    sentence = start[0] + " " + start[1]
    run = True
    while run:
        key = window.items()
        word = m.get_next_word((key[0], key[1]))
        print(word)
        if word == '[stop]':
            break
        sentence += " " + word
        window.dequeue()
        window.enqueue(word)

    return sentence


