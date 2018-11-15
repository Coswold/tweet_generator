from sample import Sampling

def build_string (chain, length, start_word):
    sentence = start_word
    i = 0
    previous_word = start_word
    while i < length:
        sample = Sampling(chain[previous_word])
        sample.get_cume()
        previous_word = sample.sample()
        sentence += " " + previous_word
        i += 1

    return sentence
        
