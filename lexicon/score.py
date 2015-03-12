import sys

MAIN_PATH = "../data/aclImdb/test"
POS_PATH = MAIN_PATH + "/pos"
NEG_PATH = MAIN_PATH + "/neg"

def score(analyze):
	import operator
	from glob import glob

	for label, path, op in [('pos', POS_PATH, operator.gt), ('neg', NEG_PATH, operator.lt)]:
		correct = counter = 0
		for file in glob(path+"/*.txt"):
			# skip hidden / system files
			if file.startswith("."):
				continue
			with open(file, 'r') as f:
				if op(analyze(f.read()),0):
					correct += 1
				counter += 1
		print "%s --> Correct: %d Tested: %d Ratio: %f" % \
			(label, correct, counter, float(correct)/counter)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: %s <package.analyzer>"
		sys.exit(1)
	module,func = sys.argv[1].split('.')
	analyzer = eval("__import__('%s').%s" % (module,func))
	score(analyzer)