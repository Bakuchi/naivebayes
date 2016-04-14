import getopt
import pickle
import sys
# import dill
from tabulate import tabulate

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
        opts, args = getopt.getopt(argv, "ho:me:",
                                   ["naive=", "test_set=", "estimate=", "train_src=", "collection=", "classifier="])
    except getopt.GetoptError:
        print('Use python3 Loader.py -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h'):
            print(tabulate([['Naive bayes classifier: ', naive], ['Maximum Entropy: ', maxent],
                            ['Test set: ', test_set], ['Estimate: ', estimate],
                            ['Train set: ', train_src], ['Collection: ', collection],
                            ['Classifier: ', classifier], ['Output classifier file: ', output]],
                           headers=['Argument', 'User Input']))
            sys.exit()
        elif opt in "--src-texts":
            src_texts = arg
        elif opt in "--text-encoding":
            text_encoding = arg
        elif opt in "--word-type":
            word_type = arg
        elif opt in "-n":
            n = arg
        elif opt in "--laplace":
            laplace = True
        elif opt in "--good-turing":
            good_turing = True
        elif opt in "--unknown-word-freq":
            unk_word_freq = arg
        elif opt in "-o":
            output = arg
            # print(tabulate([['Source text: ', src_texts], ['Text encoding: ', text_encoding],
            #               ['Word type: ', word_type], ['N gramm: ', n],
            #               ['Laplace: ', laplace], ['Good-Turing: ', good_turing],
            #               ['Unknown word frequency: ', unk_word_freq], ['Output model file: ', output]],
            #              headers=['Argument', 'User Input']))

            # model = F1Helper.build_model(src_texts, text_encoding, word_type, int(n), laplace, good_turing, int(unk_word_freq))
            # print("Dumping model")
            # dump_model(model, output)
            # print("DONE, now get your model at: " + output)


def dump_model(model, output):
    f = open(output, 'wb')
    pickle.dump(model, f)
    f.close()


if __name__ == "__main__":
    main(sys.argv[1:])
