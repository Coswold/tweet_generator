import operator
import random

class Sampling (object):
	def __init__ (self, hist):
		self.cume = 0
		self.cumulative = []
		self.txt = list(hist.items())
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

	def test_sample (self):
		i = 0
		sample = {}
		while i < 1000:
			word = self.sample()
			if not word in sample:
				sample[word] = 1
			else:
				sample[word] += 1
			i += 1
		return sample
