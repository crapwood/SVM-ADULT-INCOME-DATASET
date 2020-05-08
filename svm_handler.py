from sklearn import svm
from parse_data import parse_data
from calc_error_pct import *
from sklearn.preprocessing import StandardScaler
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
training_data = os.path.join(fileDir, 'data/adult.data')
testing_data = os.path.join(fileDir, 'data/adult.test')


class SVMHandler:
    """ In this class you will implement the classifier and it's methods. """

    def __init__(self):
        self.sc = StandardScaler()
        self.classifier = svm.SVC(kernel="rbf")
        self.x_train, self.y_train = parse_data(training_data)
        self.x_test, self.y_test = parse_data(testing_data)

        # Preprocessing data aiming to achieve Gaussian with zero mean and unit variance
        self.x_train = self.sc.fit_transform(self.x_train)
        self.x_test = self.sc.transform(self.x_test)
        self.accuracy_rate = 0
        self.error_rate = 100

    def training(self):
        self.classifier.fit(self.x_train, self.y_train)

    def testing(self):
        self.accuracy_rate = self.classifier.score(self.x_test, self.y_test)
        y_pred = self.classifier.predict(self.x_test)
        self.error_rate = calculate_error_percentage(self.y_test, y_pred)
