import prune_data
import numpy as np
from sklearn import  metrics
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.cross_validation import cross_val_predict

def analyze():
    data, targets, target_names = prune_data.prune()

    print "Initiate training and classifying phase..."
    classify(data, targets, target_names)
    print "Done."


def classify(data, target, target_names):
    svm_clf = Pipeline([('vect', CountVectorizer()),
                        ('tfidf', TfidfTransformer()),
                        ('svm', LinearSVC(C=0.1))])
    svm_predicted = cross_val_predict(
            svm_clf, np.array(data), np.array(target), cv=3, n_jobs=-1)
    print(metrics.classification_report(target, svm_predicted,
        target_names=target_names))

if __name__ == "__main__":
    analyze()
