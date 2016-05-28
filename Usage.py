import Normalizer


def classify(classifier, test_text):
    test_text = Normalizer.normalize_sentence(test_text)
    classify(classifier, test_text)
    featurized_text = {i: (True) for i in test_text}
    print("Article classified as:", classifier.classify(featurized_text))
