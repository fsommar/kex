import string, os

class Lexicon(object):
    """
        Features:
            * Simple summing of sentiment words (negative .. positive)
            * Checking for negation words in the vincinity of each sentiment words
    """

    # the polarity of sentiment words is shifted if a
    # negation word is within this range of that word
    NEGATION_RANGE = 8

    # if the sentiment value is lower than this threshold
    # it will be considered negative
    POS_THRESHOLD = 3

    MAIN_PATH = os.path.dirname(__file__) + "/../data"

    # use afinn-111 as dictionary
    with open(MAIN_PATH + "/afinn/AFINN-111.txt", "r") as afinn:
        sentiment_dictionary = dict(map(lambda (k,v): \
            (k,int(v)), [line.split('\t') for line in afinn]))

    with open(MAIN_PATH + "/common/negation.txt", "r") as neg:
        negation_list = neg.read().splitlines()

    def classify(self, snippets, **kwargs):
        """
          Take a list of snippets and returns a list of polarity values.
        """
        return [self.analyze(x, **kwargs) for x in snippets]

    def analyze(self, snippet, neg_range=NEGATION_RANGE, threshold=POS_THRESHOLD):
        """
          Returns an int in the range negative .. positive representing
          the polarity value of the snippet.
        """
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
            if negate_counter >= neg_range:
                negate_flag = False
            sentiment_value = self.sentiment_dictionary.get(word, 0)
            sum += sentiment_value if not negate_flag else -1 * sentiment_value

        return sum - threshold
