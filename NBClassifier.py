from nltk import NaiveBayesClassifier, FreqDist
import Normalizer
from itertools import chain

astronomic_train = '/home/admin-r/naive/csv/training_a'
religion_train = '/home/admin-r/naive/csv/training_r'
countries_train = '/home/admin-r/naive/csv/training_c'


def build_classifier():
    ast = Normalizer.normalize(astronomic_train)
    rel = Normalizer.normalize(religion_train)
    cou = Normalizer.normalize(countries_train)
    print("Training set generation")
    training_set = [(x, "astronomy") for x in ast] + [(x, "religion") for x in rel] + [(x, "country") for x in cou]
    print("Making vocabulary")
    del ast
    del rel
    del cou
    vocabulary = FreqDist(chain(*[n for n, tag in training_set]))
    vocabulary = list(vocabulary.keys())[:100]
    print("Normalized tokens now featured")
    feature_set = [({i: (i in sentence) for i in vocabulary}, tag) for sentence, tag in training_set]
    print("Training classifier")
    classifier = NaiveBayesClassifier.train(feature_set)
    return classifier
