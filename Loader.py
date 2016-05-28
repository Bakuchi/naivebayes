import getopt
import pickle
import sys
import dill
from tabulate import tabulate
from NBClassifier import build_classifier
from Estimator import accuracy
from Usage import classify

__author__ = 'Rustem'


def main(argv):
    naive = False
    maxent = False
    logreg = False
    estimate = False
    classificate = False
    test_text = 'N\A'
    train_src = 'N\A'
    collection = 'N\A'
    classifier = "/home/admin-r/naive/pickled/new.pickle"
    output = "/home/admin-r/naive/pickled/new.pickle"
    try:
        opts, args = getopt.getopt(argv, "ho:me:nv:ts:es:tr:cl:co:",
                                   ["naive", "maxent", "test_text=", "estimate", "train_src=",
                                    "collection=", "classifier=", "output="])
    except getopt.GetoptError:
        print('Use python3 Loader.py -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt in "-h":
            print(tabulate([['Naive bayes classifier: ', naive], ['Maximum Entropy: ', maxent],
                            ['Test set: ', test_text], ['Estimate: ', estimate],
                            ['Train set: ', train_src], ['Collection: ', collection],
                            ['Classifier: ', classifier], ['Output classifier file: ', output]],
                           headers=['Argument', 'User Input']))
            sys.exit()
        elif opt in ("--naive", "-nv"):
            naive = True
        elif opt in ("--maxent", "-me"):
            maxent = True
        elif opt in ("--logreg", "-lr"):
            logreg = True
        elif opt in ("--train_src", "-tr"):
            train_src = arg
        elif opt in ("--test_text", "-tx"):
            test_text = arg
        elif opt in ("--collection", "-co"):
            collection = arg
        elif opt in ("--estimate", "-es"):
            estimate = True
        elif opt in ("--classifier", "-cl"):
            classifier = arg
        elif opt in ("-o", "--output"):
            output = arg
        elif opt in ("-u", "--usage"):
            classificate = True
        print(tabulate([['Naive bayes classifier: ', naive], ['Maximum Entropy: ', maxent],
                        ['Test text: ', test_text], ['Estimate: ', estimate],
                        ['Train set: ', train_src], ['Collection: ', collection],
                        ['Classifier: ', classifier], ['Output classifier file: ', output]],
                       headers=['Argument', 'User Input']))
    if naive:
        naive_bayes(output)
    elif maxent:
        pass
    elif estimate:
        cl = load_classifier(classifier)
        accuracy(cl)
    elif logreg:
        pass
    elif classificate:
        cl = load_classifier(classifier)
        classify(cl, test_text)


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
