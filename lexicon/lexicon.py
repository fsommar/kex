import string

"""
    Features:
        * Simple summing of sentiment words (-5 .. 5)
        * Checking for negation words in the vincinity of each sentiment words
"""
class Lexicon(object):

    def __init__(self, path="../data"):
        self.path = path
        self.run()

    def run(self):
        # use afinn-111 as dictionary
        with open(self.path + "/afinn/AFINN-111.txt", "r") as afinn:
            self.sentiment_dictionary = dict(map(lambda (k,v): \
                (k,int(v)),[line.split('\t') for line in afinn]))

        with open(self.path + "/common/negation.txt", "r") as neg:
            self.negation_list = neg.read().splitlines()

    # the polarity of sentiment words is shifted if a
    # negation word is within NEGATION.RANGE of that word
    NEGATION_RANGE = 8

    # if the sentiment value is lower than this trashold
    # it will be considered negative
    POS_TRESHOLD = 3

    def classify(self, data):
        return [self.analyze(x) for x in data]

    def analyze(self, snippet):
        # remove punctuation chars
        snippet = snippet.translate(None, string.punctuation)
        words = snippet.lower().split()
        sum = 0
        negate_flag = False
        negate_counter = 0
        for word in words:
            if word in self.negation_list:
                negate_flag = True
                negate_counter = 0
                continue
            negate_counter += 1
            if negate_counter >= self.NEGATION_RANGE:
                negate_flag = False
            sentiment_value = self.sentiment_dictionary.get(word, 0)
            sum += sentiment_value if not negate_flag else -1 * sentiment_value

        return sum - self.POS_TRESHOLD
