# vim: tabstop=2 softtabstop=2 shiftwidth=2 expandtab
from sklearn import metrics
from hybrid import split_data, mid
from learning import learning
from lexicon import Lexicon
import os

MAIN_PATH = os.path.dirname(__file__)

# only a most informative percentage of the data will
# be used in training the learning classifier
MID_RATIO = 0.3

# Remove?
LEXICON_THRESHOLD = 0

def main():
  """
    Split the dataset into two sets; validation and training.

    Lexicon:    run lexicon clf on validation data and cmp it with validation
                target.

    Learning:   train learning clf on traning data, run it on validation data
                and cmp it with validation target.

    Hybrid:     run lexicon clf on training data, train learning clf on the
                lexicon target output, run the learning clf on validation data
                and cmp it with validation target.
  """

  #### PREPARE THE DATA SETS ####
  print "Split data..."
  validation, training = split_data.split()

  #### LEXICON-BASED APPROACH ####
  print "Lexicon..."
  lexicon = Lexicon()
  lex_predicted = lexicon.classify(validation["data"], threshold=LEXICON_THRESHOLD)
  lex_expected, _, lex_predicted = mid.prune(validation["target"], validation["data"], lex_predicted)

  #### LEARNING-BASED APPROACH ####
  print "Learning..."
  learning_clf = learning.train(training["data"], training["target"])
  learning_predicted = learning_clf.predict(validation["data"])
  learning_expected = validation["target"]

  #### COMBINED, HYBRID APPROACH ####
  print "Hybrid..."
  hybrid_lex_target = lexicon.classify(training["data"], threshold=LEXICON_THRESHOLD)
  _, hybrid_data, hybrid_lex_predicted = mid.prune(validation["target"], training["data"], hybrid_lex_target, ratio=MID_RATIO)

  hybrid_clf = learning.train(hybrid_data, hybrid_lex_predicted)
  hybrid_predicted = hybrid_clf.predict(validation["data"])
  hybrid_expected = validation["target"]

  #### PRINT METRICS ####
  target_names = ["neg", "pos"]
  print "Lexicon"
  print(metrics.classification_report(lex_expected, lex_predicted, target_names=target_names))
  print "Learning"
  print(metrics.classification_report(learning_expected, learning_predicted,
        target_names=target_names))
  print "Hybrid"
  print(metrics.classification_report(hybrid_expected, hybrid_predicted,
        target_names=target_names))

if __name__ == "__main__":
  main()
