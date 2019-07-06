from dictogram import Dictogram
from sample import Sampling

class Markov (object):

    def __init__(self, txt):
        self.hist = {}
        self.start = Dictogram()
        self.build(txt)

    def build(self, txt):
        i = 0
        # Build initial histogram
        while i < len(txt) - 2:
            words = (txt[i + 1], txt[i + 2])
            if txt[i] == '[start]':
                self.start.add_count(words)
            i += 1

        i = 0
        while i < len(txt) - 2:
            key = (txt[i], txt[i + 1])
            if key not in self.hist:
                self.hist[key] = Dictogram()
            self.hist[key].add_count(txt[i + 2])
            i += 1

    def get_start(self):
        sample = Sampling(self.start)
        sample.get_cume()
        start = sample.sample()
        return start

    def get_next_word(self, key):
        sample = Sampling(self.hist[key])
        sample.get_cume()
        word = sample.sample()
        return word

