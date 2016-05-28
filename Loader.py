import getopt, pickle, sys
from nltk import NaiveBayesClassifier, MaxentClassifier
from tabulate import tabulate
from Estimator import accuracy
from Classifier import classify, build_classifier

__author__ = 'Rustem'


def main(argv):
    naive = False
    maxent = False
    estimate = False
    precision = False
    classificate = False
    text = 'N\A'
    classifier = "/home/admin-r/naive/pickled/new.pickle"
    output = "/home/admin-r/naive/pickled/new.pickle"
    try:
        opts, args = getopt.getopt(argv, "ho:mo:no:t:eo:l:co:po:oo",
                                   ["maxent", "naive", "text=", "estimate",
                                    "classifier=", "classify", "precision", "output="])
    except getopt.GetoptError:
        print('Use python3 Loader.py -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt in "-h":
            print(tabulate([['To train naive bayes classifier type', "-n | --naive"],
                            ['To train Maximum Entropy classifier type ', "-m | --maxent"],
                            ['To estimate accuracy type ', "-e | --estimate"],
                            ['If you additionally want to calculate precision type', "-p | --precision"],
                            ['To classify type ', "-c | --classify"],
                            ['Then load your classifier with ', "-l | --classifier"],
                            ['And type text path with', "-t | --text /path/to/text/"],
                            ['To change classifier output file type ', "-o | --output"]],
                           headers=['Description', 'Args']))
            sys.exit()
        elif opt in ("--naive", "-n"):
            naive = True
        elif opt in ("--maxent", "-m"):
            maxent = True
        elif opt in ("--estimate", "-e"):
            estimate = True
        elif opt in ("--precision", "-p"):
            precision = True
        elif opt in ("--classify", "-c"):
            classificate = True
        elif opt in ("--classifier", "-l"):
            classifier = arg
        elif opt in ("--text", "-t"):
            text = arg
        elif opt in ("--output", "-o"):
            output = arg

    if naive:
        print("Building new classifier based on Naive Bayes")
        classifier = build_classifier(NaiveBayesClassifier)
        dump_classifier(classifier, output)
    elif maxent:
        print("Building new classifier based on Max Entropy")
        classifier = build_classifier(MaxentClassifier)
        dump_classifier(classifier, output)
    elif estimate:
        cl = load_classifier(classifier)
        accuracy(cl, precision)
    elif classificate:
        cl = load_classifier(classifier)
        classify(cl, text)


def dump_classifier(classifier, output):
    print("Dumping classifier to file", output)
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
