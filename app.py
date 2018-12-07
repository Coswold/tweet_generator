from flask import Flask
import sys
import random
from clean import strip_pun, read
from markov_chain import markov
from build_string import build_string
from dictogram import Dictogram
from sample import Sampling
from queue import Queue

app = Flask(__name__)

@app.route("/")
def home():
    txt = read(sys.argv[1])
    order = int(sys.argv[2])
    rand = random.randrange(0, len(txt) - 1)
    window = Queue()
    i = 0
    while i < order:
        window.enqueue(txt[rand + i])
        i += 1 
    sentence = build_string(20, window, txt)

    return sentence	 

if __name__ == "__main__":
	app.run()
