import Normalizer


def classify(classifier, test_text):
    test_text = [item for sublist in Normalizer.normalize(test_text) for item in sublist]
    featurized_text = {i: (True) for i in test_text}
    print("Article classified as:", classifier.classify(featurized_text))
