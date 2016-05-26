import nltk
import nltk.classify.scikitlearn
from nltk.tokenize import word_tokenize
astronomic = '/home/admin-r/naive/csv/astronomical.txt'
religion = '/home/admin-r/naive/csv/religion.txt'
countries = '/home/admin-r/naive/csv/country.txt'
homePATH = '/home/admin-r/naive/csv/'
ids = []


def read_file(path):
    with open(path, newline='') as f:
        for row in f:
            ids.append((row,'country'))
read_file(countries)
all_words = set(word.lower() for passage in ids[:40] for word in word_tokenize(passage[0]))
t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in ids]
print(t)
