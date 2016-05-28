from itertools import chain

import Normalizer
from nltk import FreqDist, classify

astronomic_test = '/home/admin-r/naive/csv/test_a'
religion_test = '/home/admin-r/naive/csv/test_r'
countries_test = '/home/admin-r/naive/csv/test_c'


def accuracy(classifier):
    print("====== ESTIMATING CLASSIFIER ACCURACY ======")
    ast = Normalizer.normalize(astronomic_test)
    rel = Normalizer.normalize(religion_test)
    cou = Normalizer.normalize(countries_test)
    print("Test set generation")
    test_set = [(x, "astronomy") for x in ast] + [(x, "religion") for x in rel] + [(x, "country") for x in cou]
    del ast
    del rel
    del cou
    vocabulary = FreqDist(chain(*[n for n, tag in test_set]))
    vocabulary = list(vocabulary.keys())[:100]
    feature_set = [({i: (i in sentence) for i in vocabulary}, tag) for sentence, tag in test_set]
    print("Trained classifier estimated accuracy:", classify.accuracy(classifier, feature_set))
