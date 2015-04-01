import prune_data
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

def analyze():
    # data, targets, target_names = prune_data.prune()

    data = [
        u"Hello i like ice cream",
        u"Me too i love ice cream",
        u"i really hate ice cream"
    ]
    targets = [0,0,1]
    target_names = ['pos','neg']
    classify(data, targets, target_names, data)


def classify(data, targets, target_names, test_data):
    print type(targets)
    svm_clf = Pipeline([('vect', CountVectorizer()),
                        ('tfidf', TfidfTransformer()),
                        ('svm', LinearSVC())])
    svm_clf = svm_clf.fit(data, targets)
    svm_predicted = svm_clf.predict(test_data)
    print(metrics.classification_report(targets, svm_predicted,
        target_names=target_names))

if __name__ == "__main__":
    analyze()
