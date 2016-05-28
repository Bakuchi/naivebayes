import nltk, mmap, string
from nltk.stem import SnowballStemmer

translator = str.maketrans({key: None for key in string.punctuation})
default_stopwords = set(nltk.corpus.stopwords.words('russian'))


def clear(tokenlist):
    print("LOWERCASING AND CLEARING tokenlist from stop words")
    tokens = tokenlist
    tokens = [word.lower() for word in tokens]
    tokens = [word for word in tokens if word not in default_stopwords]
    return tokens


def remove_punctuation(text):
    return text.translate(translator)


def surface_no_pm(text):
    corpus = remove_punctuation(text)
    return clear(nltk.WordPunctTokenizer().tokenize(corpus))

def stemmed(text):
    stemmer = SnowballStemmer("russian")
    nonstemmed = surface_no_pm(text)
    return clear([stemmer.stem(w) for w in nonstemmed])

def process_tokenization(text):
    print("NOW TOKENIZING")
    tokens = stemmed(text)
    return tokens


def normalize(root):
    tokens = []
    line = 0
    with open(root, 'r') as f:
        m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
        data = m.readline()
        while data:
            line += 1
            enc = data.decode("utf-8")
            tokens.append(process_tokenization(enc))
            print("Reading  " + str(line) + " line of the training file")
            data = m.readline()
    print("tokens out")
    return tokens

def normalize_sentence(root):
    tokens = []
    line = 0
    with open(root, 'r') as f:
        m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
        data = m.readline()
        while data:
            line += 1
            enc = data.decode("utf-8")
            tokens.extend(process_tokenization(enc))
            print("Reading  " + str(line) + " line of the training file")
            data = m.readline()
    print("tokens out")
    return tokens

