from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

# data: np.array
# target: np.array
# returns a classifier `clf` which can be used with predicted_target = clf.predict(data)
def train(data, target):
    svm_clf = Pipeline([('vect', CountVectorizer()),
                        ('tfidf', TfidfTransformer()),
                        ('svm', LinearSVC(C=0.1))])
    svm_clf.fit_transform(data, target)
    return svm_clf
