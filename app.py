from flask import Flask
import sys
from clean import strip_pun, read
from markov_chain import markov
from build_string import build_string
from dictogram import Dictogram
from sample import Sampling

app = Flask(__name__)

@app.route("/")
def home():
    txt = read(sys.argv[1])
    g_dict = Dictogram(txt)
    sample = Sampling(g_dict)
    sample.get_cume()
    first_word = sample.sample()
    sentence = build_string(10, first_word, txt)

    return sentence	 

if __name__ == "__main__":
	app.run()
