import prune_data
import numpy as np
from sklearn import  metrics
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.cross_validation import train_test_split

def analyze():
    data, targets, target_names = prune_data.prune()

    classify(data, targets, target_names)


def classify(data, target, target_names):
    train_data, test_data, train_target, test_target  = train_test_split(data, target, test_size=0.5)
    svm_clf = Pipeline([('vect', CountVectorizer()),
                        ('tfidf', TfidfTransformer()),
                        ('svm', LinearSVC())])
    svm_clf = svm_clf.fit(train_data, train_target)
    svm_predicted = svm_clf.predict(test_data)
    print(metrics.classification_report(test_target, svm_predicted,
        target_names=target_names))

if __name__ == "__main__":
    analyze()
