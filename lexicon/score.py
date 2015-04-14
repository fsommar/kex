# vim: tabstop=2 softtabstop=2 shiftwidth=2 expandtab
import sys, operator, os

MAIN_PATH = os.path.dirname(__file__) + "/../data/aclImdb/test"
VERBOSE = False

"""
  Runs on assumption 1 text snippet / file.
"""
def score(analyze, tests=[]):
  from glob import glob

  POS_PATH = MAIN_PATH + "/pos"
  NEG_PATH = MAIN_PATH + "/neg"

  # default tests both positive and negative
  if not tests:
    tests = ['pos','neg']
  classes = [('pos', POS_PATH, operator.gt), ('neg', NEG_PATH, operator.lt)]

  res = "\nResults:\n"
  tp = tn = fn = fp = 0

  for label, path, op in classes:
    if label not in tests:
      continue


    print "Compiling file list... (%s)" % label
    files = glob(path+"/[!.]*.txt")
    files_len = len(files)

    print "Analyzing files... (%s)" % label
    correct = counter = 0
    for file in files:
      with open(file, 'r') as f:
        if op(analyze(f.read()),0):
          correct += 1
        counter += 1
      if VERBOSE and counter % 100 == 0:
        print "Analyzed %d/%d snippets" % (counter, files_len)

    # Gather results
    if counter < 1:
      res += "%s ---> no tests were run.\n" % label
    else:
      res += "%s --> Correct: %6d Tested: %6d Ratio: %6.3f\n" % \
        (label, correct, counter, float(correct)/counter)
      if label == classes[0][0]:
        # positives, calculate False Negatives
        fn = counter - correct
        tp = counter
      else:
        # negatives, calculate False Positives
        fp = counter - correct
        tn = counter

  print res

  if (tp != 0):
      precision = float(tp)/(tp + fn)
      recall = float(tp)/(tp + fp)
      print "Precision: %f\nRecall: %f" % (precision, recall)
      print "F-score: %f" % (2*precision*recall/(precision+recall))


if __name__ == '__main__':
  if len(sys.argv) < 2:
    print "Usage: %s [-v] <package.classifier> [tests]" % sys.argv[0]
    print "The classifier must contain a method 'analyze'" + \
      "\nwhich takes a text snippet as its only argument."
    sys.exit(1)

  idx = 1
  if sys.argv[1] == "-v":
    idx += 1
    VERBOSE = True
  module,func = sys.argv[idx].split('.')
  classifier = eval("__import__('%s').%s" % (module,func))
  analyze = classifier().analyze
  tests = sys.argv[idx+1:]
  score(analyze, tests)
