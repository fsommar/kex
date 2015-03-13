import sys, operator

MAIN_PATH = "../data/aclImdb/test"
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

  res = "\nResults:\n"
  for label, path, op in [('pos', POS_PATH, operator.gt), ('neg', NEG_PATH, operator.lt)]:
    if label not in tests:
      continue
    correct = counter = 0
    print "Compiling file list..."
    files = glob(path+"/[!.]*.txt")
    print "Analyzing files..."
    files_len = len(files)
    for file in files:
      with open(file, 'r') as f:
        if op(analyze(f.read()),0):
          correct += 1
        counter += 1
      if VERBOSE and counter % 100 == 0:
        print "Analyzed %d/%d snippets" % (counter, files_len)
    if counter < 1:
      res += "%s ---> no tests were run.\n" % label
    else:
      res += "%s --> Correct: %6d Tested: %6d Ratio: %6.3f\n" % \
        (label, correct, counter, float(correct)/counter)

  print res

"""
  Run on assumption multiple text snippets in
  one file separated by '####'.
"""
def score_merged(analyze, tests=[]):
  DELIM = "####"
  POS_PATH = MAIN_PATH + "/pos_merged.txt"
  NEG_PATH = MAIN_PATH + "/neg_merged.txt"

  # default tests both positive and negative
  if not tests:
    tests = ['pos','neg']

  for label, path, op in [('pos', POS_PATH, operator.gt), ('neg', NEG_PATH, operator.lt)]:
    if label not in tests:
      continue
    correct = counter = 0
    with open(path, 'r') as f:
      for snippet in f.read().split(DELIM):
        if op(analyze(snippet),0):
          correct += 1
        counter += 1
    if counter < 1:
      print "%s ---> no tests were run." % label
    else:
      print "%s --> Correct: %d Tested: %d Ratio: %f" % \
        (label, correct, counter, float(correct)/counter)        

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