from flask import Flask, render_template
from clean import strip_pun, read
from build_string import build_string
from grammar import grammar

app = Flask(__name__)

@app.route("/")
def home():
    txt = read("static/buddha.txt")
    sentence = build_string(txt)
    sentence = grammar(sentence)

    return render_template("template.html", sentence = sentence)

if __name__ == "__main__":
	app.run()
