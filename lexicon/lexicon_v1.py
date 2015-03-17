"""
    Features:
        * Simple summing of weighted words (-5 .. 5)
"""
class Lexicon(object):

    # use afinn-111 as dictionary
    with open("../data/afinn/AFINN-111.txt", "r") as afinn:
        dictionary = dict(map(lambda (k,v): (k,int(v)),[line.split('\t') for line in afinn]))

    def analyze(self, sentence):
        return sum(map(lambda word: self.dictionary.get(word, 0), sentence.lower().split()))
