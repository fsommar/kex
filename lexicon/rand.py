from random import choice

class Random(object):

	def analyze(self, sentence):
		# either positive or negative at random
		return choice([-1,1])