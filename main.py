# vim: tabstop=2 softtabstop=2 shiftwidth=2 expandtab
from sklearn import metrics
from hybrid import split_data, mid
from learning import learning
from lexicon.lexicon import Lexicon

def main():
  # grab data
  print "Split data..."
  validation, training = split_data.split("data/aclImdb/test")

  # lexicon-based approach
  print "Lexicon..."
  lexicon = Lexicon("data")
  lex_predicted = lexicon.classify(validation["data"])
  lex_expected, _, lex_predicted = mid.prune(validation["target"], training["data"], lex_predicted)

  # learning-based approach
  print "Learning..."
  learning_clf = learning.train(training["data"], training["target"])
  learning_predicted = learning_clf.predict(validation["data"])
  learning_expected = validation["target"]

  # combined, hybrid approach
  print "Hybrid..."
  hybrid_lex_target = lexicon.classify(training["data"])
  _, hybrid_data, hybrid_lex_predicted = mid.prune(validation["target"], training["data"], hybrid_lex_target, ratio=0.4)

  hybrid_clf = learning.train(hybrid_data, hybrid_lex_predicted)
  hybrid_predicted = hybrid_clf.predict(validation["data"])
  hybrid_expected = validation["target"]

  # print metrics
  target_names = ["pos", "neg"]
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
