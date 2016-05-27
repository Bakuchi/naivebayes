from nltk import NaiveBayesClassifier
import Normalizer
from itertools import chain

astronomic_train = '/home/admin-r/naive/csv/training_a'
astronomic_test = '/home/admin-r/naive/csv/test_a'
religion_train = '/home/admin-r/naive/csv/training_r'
religion_test = '/home/admin-r/naive/csv/test_r'
countries_train = '/home/admin-r/naive/csv/training_c'
countries_test = '/home/admin-r/naive/csv/test_c'
homePATH = '/home/admin-r/naive/csv/'
vocabulary = ()

def build_classifier(train):
    text = Normalizer.normalize(train)
    print("Normalized tokens now featured")
    tag = 'c'
    vocabulary = set(text)
    feature_set = [({i:(i in text) for i in vocabulary}, tag)]
    print("classifying")
    classifier = NaiveBayesClassifier.train(feature_set)
    return classifier

classifier = build_classifier(countries_train)
test_sentence = "This is the best band I've ever heard!"
featurized_test_sentence = {i: (i in Normalizer.normalize(test_sentence)) for i in vocabulary}
print ("test_sent:",test_sentence)
print(featurized_test_sentence)
print ("tag:",classifier.classify(featurized_test_sentence))