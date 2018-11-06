import sys
import random
import operator

class Logger (object):
	def __init__(self, file_name):
		self.file_name = file_name

	def log_data(self, words, max_word, word_list):
		self.file = open(self.file_name, "w+")
		#self.file.write("The text has {} unique words\nThe most common word is [{}], appearing {} times\n\n".format(words, max_word[0], max_word[1]))
		for i, j in word_list.items():
			self.file.write("{}: {}\n".format(i, j))
		self.file.close()	

class Analysis (object):
	def __init__ (self):
		self.txt_file = ""
		self.word_list = {}
		self.number_unique_words = 0
		self.total_words = 0

	def strip_pun (self, string):
		punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		no_punc = ""

		for char in string:
			if char not in punc:
				no_punc += char

		return no_punc
	
	def get_total_words (self):
		for i in self.word_list:
			self.total_words += self.word_list[i]
		return self.total_words
		
	def read (self, txt):
		f = open(txt, "r")
		contents = f.read()
		f.close()
		contents = contents.lower()
		contents = self.strip_pun(contents)
		self.txt_file = contents.split()
		return self.txt_file

	def histogram (self):
		for i in self.txt_file:
			if not i in self.word_list:
				self.word_list[i] = 1
			else:
				self.word_list[i] += 1
		return self.word_list

	def unique_words (self):
		for _ in self.word_list:
			self.number_unique_words += 1
		return self.number_unique_words 

	def frequency (self):
		word_search = input("What word would you like to search?\n").lower()
		if not word_search in self.word_list:
			return "Word not found"
		else:
			word = self.word_list[word_search]
			prob = word/self.total_words
			return word, prob
	
	def max_word (self):
		maxi = 0
		for i in self.word_list:
			if self.word_list[i] > maxi:
				maxi = self.word_list[i]
				word = i
		return word, maxi

	def mean (self):
		return self.total_words / self.number_unique_words

class Sampling (object):
	def __init__ (self):
		self.txt = []
		self.cume = 0
		f = open("histogram.txt", "r")
		self.cumulative = []
		for line in f:
			k, v = line.strip().split(':')
			self.txt.append((k, int(v)))

		f.close()
		self.txt.sort(key = operator.itemgetter(1))
		
	def get_cume (self):
		for i in self.txt:
			self.cume += i[1]
			self.cumulative.append((i[0], self.cume))

	def sample (self):
		rand = random.randrange(0, self.cume)
		for i in self.cumulative:
			if i[1] > rand:
				return i[0]

if __name__ == '__main__':
	analysis = Analysis()
	logger = Logger("histogram.txt")
	analysis.read(sys.argv[1])
	analysis.histogram()
	analysis.get_total_words()
	print("\x1b[2J\x1b[H")
	print("Total words: \x1b[36m{}\x1b[0m".format(str(analysis.total_words)))
	print("Unique words: \x1b[36m{}\x1b[0m".format(str(analysis.unique_words())))
	most = analysis.max_word()
	print("Most common word is \x1b[32m{}\x1b[0m appearing \x1b[36m{}\x1b[0m times".format(most[0], most[1]))
	print("Mean number of words appearing: \x1b[36m{}\x1b[0m".format(str(analysis.mean())))
	logger.log_data(analysis.number_unique_words, most, analysis.word_list)
	print(analysis.frequency())
	sampler = Sampling()
	sampler.get_cume()
	print(sampler.sample())
				
