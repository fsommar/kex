# use afinn-111 as dictionary
with open("../data/afinn/AFINN-111.txt", "r") as afinn:
	dictionary = dict(map(lambda (k,v): (k,int(v)),[line.split('\t') for line in afinn]))

def analyze(sentence):
	return sum(map(lambda word: dictionary.get(word, 0), sentence.lower().split()))