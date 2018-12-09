from flask import Flask, render_template
import sys
import random
from clean import strip_pun, read
from markov_chain import markov
from build_string import build_string
from dictogram import Dictogram
from sample import Sampling
from queue import Queue
from grammar import grammar

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
    sentence = build_string(30, window, txt)
    sentence = grammar(sentence)

    return render_template("template.html", sentence = sentence)	 

if __name__ == "__main__":
	app.run()
