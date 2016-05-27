from nltk import NaiveBayesClassifier, FreqDist
import Normalizer
from itertools import chain

astronomic_train = '/home/admin-r/naive/csv/training_a'
astronomic_test = '/home/admin-r/naive/csv/test_a'
religion_train = '/home/admin-r/naive/csv/training_r'
religion_test = '/home/admin-r/naive/csv/test_r'
countries_train = '/home/admin-r/naive/csv/training_c'
countries_test = '/home/admin-r/naive/csv/test_c'
homePATH = '/home/admin-r/naive/csv/'

def build_classifier(train):
    ast = Normalizer.normalize(astronomic_train)
    rel = Normalizer.normalize(religion_train)
    cou = Normalizer.normalize(countries_train)
    print("Training set generation")
    print(len(rel))
    print(len(ast))
    print(len(cou))
    training_set = [(x, "astronomy") for x in ast]+[(x, "religion") for x in rel]+[(x, "country") for x in cou]
    print("vocab")
    del ast
    del rel
    del cou
    vocabulary = FreqDist(chain(*[n for n, tag in training_set]))
    vocabulary = list(vocabulary.keys())[:650]
    # print(vocabulary)
    # print(len(vocabulary))
    print("Normalized tokens now featured")
    feature_set = [({i: (i in sentence) for i in vocabulary}, tag) for sentence, tag in training_set]
    # feature_set = [({i: (i in list) for i in vocabulary}, tag) for list, tag in
    #                training_set]
    # feature_set = [({i:(i in text) for i in vocabulary}, tag)]
    print("classifying")
    classifier = NaiveBayesClassifier.train(feature_set)
    test_cl(classifier,vocabulary)
    return classifier

def test_cl(classifier,vocabulary):
    test_sentence = '/home/admin-r/naive/csv/11'
    test_sentence = Normalizer.normalize2(test_sentence)
    featurized_test_sentence = {i: (i in test_sentence) for i in vocabulary}
    print ("test_sent:",test_sentence)
    print(featurized_test_sentence)
    print ("tag:", classifier.classify(featurized_test_sentence))
