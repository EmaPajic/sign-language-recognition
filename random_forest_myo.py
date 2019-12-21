"""
@author: EmaPajic
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import read_samples
from sklearn import metrics

def main():
    X_training, Y_training = read_samples.read_periodogram_training()
    X_test, Y_test = read_samples.read_periodogram_test()

    
    clf = RandomForestClassifier(n_estimators=100, max_depth=14, random_state=0)
    clf.fit(X_training, Y_training)
    
    # Use the forest's predict method on the test data
    predictions = clf.predict(X_test)

    errors = 0
    for i in range(0, len(predictions)):
        if predictions[i] != Y_test[i]:
            errors += 1
            
    accuracy = 100 - 100 * errors / len(predictions)
    print(accuracy)
    
    print("Classification report for classifier %s:\n%s\n"% (clf, metrics.classification_report(Y_test, predictions)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(Y_test, predictions))
        
if __name__ == '__main__':
    main()
    