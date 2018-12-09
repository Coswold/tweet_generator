def grammar (sentence):
    sentence = sentence.capitalize()
    if sentence[len(sentence) - 1] == ',':
        sentence[len(sentence) - 1] == '.'
    else:
        sentence += '.'
    return sentence
