"""
@author: EmaPajic
"""

import numpy as np
import read_samples
from sklearn import metrics

from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)


def main():
    X_train, Y_train = read_samples.read_periodogram_training()
    X_test, Y_test = read_samples.read_periodogram_test()

    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    model.fit(X_train, Y_train, epochs=150, batch_size=10)
    
    predictions = model.predict(X_test)
    errors = 0
    for i in range(0, len(predictions)):
        if predictions[i] != Y_test[i]:
            errors += 1
            
    accuracy = 100 - 100 * errors / len(predictions)
    print(accuracy)
    
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(Y_test, predictions))
        
if __name__ == '__main__':
    main()
    