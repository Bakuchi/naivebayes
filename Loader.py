import getopt
import pickle
import sys
import dill
from tabulate import tabulate
from NBClassifier import build_classifier
from Estimator import accuracy
from Classifier import classify

__author__ = 'Rustem'


def main(argv):
    naive = False
    classificate = False
    precision = False
    estimate = False
    maxent = False
    logreg = False
    text = 'N\A'
    classifier = "/home/admin-r/naive/pickled/new.pickle"
    output = "/home/admin-r/naive/pickled/new.pickle"
    try:
        opts, args = getopt.getopt(argv, "ho:mo:no:t:eo:l:ro:co:po:oo",
                                   ["maxent", "naive", "text=", "estimate", "regression",
                                    "classifier=", "classificate", "precision", "output="])
    except getopt.GetoptError:
        print('Use python3 Loader.py -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt in "-h":
            print(tabulate([['Naive bayes classifier: ', naive], ['Maximum Entropy: ', maxent],
                            ['Test set: ', text], ['Estimate: ', estimate],
                            ['Classifier: ', classifier], ['Output classifier file: ', output]],
                           headers=['Argument', 'User Input']))
            sys.exit()
        elif opt in ("--naive", "-n"):
            naive = True
        elif opt in ("--maxent", "-m"):
            maxent = True
        elif opt in ("--regression", "-r"):
            logreg = True
        elif opt in ("--text", "-t"):
            text = arg
        elif opt in ("--estimate", "-e"):
            estimate = True
        elif opt in ("--classifier", "-l"):
            classifier = arg
        elif opt in ("-o", "--output"):
            output = arg
        elif opt in ("-c", "--classificate"):
            classificate = True
        elif opt in ("-p", "--precision"):
            precision = True
        print(tabulate([['Naive bayes classifier: ', naive], ['Maximum Entropy: ', maxent],
                        ['Test text: ', text], ['Estimate: ', estimate],
                        ['Calculate: ', precision],
                        ['Classifier: ', classifier], ['Output classifier file: ', output]],
                       headers=['Argument', 'User Input']))
    if naive:
        naive_bayes(output)
    elif maxent:
        pass
    elif estimate:
        cl = load_classifier(classifier)
        accuracy(cl, precision)
    elif logreg:
        pass
    elif classificate:
        cl = load_classifier(classifier)
        classify(cl, text)


def naive_bayes(out):
    print("Building new classifier based on Naive Bayes")
    classifier = build_classifier()
    print("dumping")
    dump_classifier(classifier, out)


def dump_classifier(classifier, output):
    f = open(output, 'wb')
    pickle.dump(classifier, f)
    f.close()
    print("Dump success")


def load_classifier(path):
    with open(path, 'rb') as pickle_file:
        classifier = pickle.load(pickle_file)
    return classifier


if __name__ == "__main__":
    main(sys.argv[1:])
