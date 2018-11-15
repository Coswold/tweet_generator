from random import shuffle
import sys

def re_arrange (words):
	shuffle(words)
	return words

if __name__ == '__main__':
	random = []
	i = 1
	while i < len(sys.argv):
		random.append(sys.argv[i])
		i += 1
	words = re_arrange(random)
	for i in words:
		print(i)
	print(random)
		
