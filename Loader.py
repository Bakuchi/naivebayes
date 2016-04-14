import getopt
import pickle
import sys
import dill
from tabulate import tabulate
from NBClassifier import build_classifier

__author__ = 'Rustem'


def main(argv):
    naive = False
    maxent = False
    test_set = 'N\A'
    estimate = False
    train_src = 'N\A'
    collection = 'N\A'
    classifier = False
    output = "/home/admin-r/naive/pickled/new.pickle"
    try:
        opts, args = getopt.getopt(argv, "ho:me:nv:ts:es:tr:cl:co:",
                                   ["naive", "maxent", "test_set=", "estimate", "train_src=",
                                    "collection=", "classifier=", "output="])
    except getopt.GetoptError:
        print('Use python3 Loader.py -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt in "-h":
            print(tabulate([['Naive bayes classifier: ', naive], ['Maximum Entropy: ', maxent],
                            ['Test set: ', test_set], ['Estimate: ', estimate],
                            ['Train set: ', train_src], ['Collection: ', collection],
                            ['Classifier: ', classifier], ['Output classifier file: ', output]],
                           headers=['Argument', 'User Input']))
            sys.exit()
        elif opt in ("--naive", "-nv"):
            naive = True
        elif opt in ("--maxent", "-me"):
            maxent = True
        elif opt in ("--train_src", "-tr"):
            train_src = arg
        elif opt in ("--test_set", "-ts"):
            test_set = arg
        elif opt in ("--collection", "-co"):
            collection = arg
        elif opt in ("--estimate", "-es"):
            estimate = True
        elif opt in ("--classifier", "-cl"):
            classifier = arg
        elif opt in ("-o", "--output"):
            output = arg
        print(tabulate([['Naive bayes classifier: ', naive], ['Maximum Entropy: ', maxent],
                        ['Test set: ', test_set], ['Estimate: ', estimate],
                        ['Train set: ', train_src], ['Collection: ', collection],
                        ['Classifier: ', classifier], ['Output classifier file: ', output]],
                       headers=['Argument', 'User Input']))

        # model = F1Helper.build_model(src_texts, text_encoding, word_type, int(n), laplace, good_turing, int(unk_word_freq))
        # print("Dumping model")
        # dump_model(model, output)
        # print("DONE, now get your model at: " + output)
    if naive:
        naive_bayes(train_src, output)
    elif maxent:
        pass
    elif estimate:
        pass


def naive_bayes(train, out):
    print("Building new classifier based on Naive Bayes")
    classifier = build_classifier(train)
    dump_classifier(classifier, out)


def dump_classifier(classifier, output):
    f = open(output, 'wb')
    pickle.dump(classifier, f)
    f.close()
    print("Dump success")


if __name__ == "__main__":
    main(sys.argv[1:])
