from flask import Flask
import sys
from word_frequency import Analysis, Logger, Sampling

app = Flask(__name__)

def build_sentence (sampler):
	sentence = ""
	i = 0
	while i < 10:
		sentence += sampler.sample() + " "
		i += 1
	return sentence


def build_data ():
	analysis = Analysis()
	logger = Logger("histogram.txt")
	analysis.read(sys.argv[1])
	analysis.histogram()
	analysis.get_total_words()
	most = analysis.max_word()
	logger.log_data(analysis.number_unique_words, most, analysis.word_list)
	sampler = Sampling()
	sampler.get_cume()
	sentence = build_sentence(sampler)
	return sentence

@app.route("/")
def home():
	return build_data()		 

if __name__ == "__main__":
	app.run()
