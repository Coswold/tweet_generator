import random
import sys

class Create_sentence (object):
	def __init__(self):
		self.dict = ""
		self.sentence = []
	
	def get_dict (self, txt_file):
		f = open(txt_file, "r")
		contents = f.read()
		f.close()
		self.dict = contents.split()
		return contents

	def get_word (self):
		random_word = random.choice(self.dict)
		return random_word
	
	def build_sentence (self, nbr_words):
		i = 0
		while i < nbr_words:
			self.sentence.append(self.get_word())
			i += 1
		return self.sentence

	def print_sentence (self):
		for i in self.sentence:
			sys.stdout.write(i + " ")
		print("")

if __name__ == '__main__':
	new_sentence = Create_sentence()
	length = int(sys.argv[2])
	new_sentence.get_dict(sys.argv[1])
	new_sentence.build_sentence(length)
	new_sentence.print_sentence()
