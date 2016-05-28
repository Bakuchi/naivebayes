from itertools import chain

import collections

import Normalizer
from nltk import FreqDist, classify, metrics

astronomic_test = '/home/admin-r/naive/csv/test_a'
religion_test = '/home/admin-r/naive/csv/test_r'
countries_test = '/home/admin-r/naive/csv/test_c'


def accuracy(classifier, calc):
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
    if (calc):
        calculate(classifier, feature_set)

def calculate(classifier, feature_set):
    refsets = collections.defaultdict(set)
    testsets = collections.defaultdict(set)

    print("Calculating refsets for precision and recall")
    for i, (feats, label) in enumerate(feature_set):
        refsets[label].add(i)
        observed = classifier.classify(feats)
        testsets[observed].add(i)

    print('country precision:', metrics.precision(refsets['country'], testsets['country']))
    print('country recall:', metrics.recall(refsets['country'], testsets['country']))

    print('religion precision:', metrics.precision(refsets['religion'], testsets['religion']))
    print('religion recall:', metrics.recall(refsets['religion'], testsets['religion']))

    print('astronomy precision:', metrics.precision(refsets['astronomy'], testsets['astronomy']))
    print('astronomy recall:', metrics.recall(refsets['astronomy'], testsets['astronomy']))


