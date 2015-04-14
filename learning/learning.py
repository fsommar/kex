from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

def train(data, target):
    """
      Trains a classifier and returns it.

      The classifier can then be used as predicted_target = clf.predict(data)

      Parameters:
            data    - a np.array with snippets
            target  - a np.array with targets (0 - neg, 1 - pos)
    """
    svm_clf = Pipeline([('vect', CountVectorizer()),
                        ('tfidf', TfidfTransformer()),
                        ('svm', LinearSVC(C=0.1))])
    svm_clf.fit_transform(data, target)
    return svm_clf
