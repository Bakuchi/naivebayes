import wikipedia, csv

wikipedia.set_lang("ru")
astronomicCSV = '/home/admin-r/naive/csv/astronomical'
religionCSV = '/home/admin-r/naive/csv/religion'
countriesCSV = '/home/admin-r/naive/csv/countries'
homePATH = '/home/admin-r/naive/csv/'
DisambiguationErrorItems = []


def read_pageids(path):
    ids = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids.append((row['pageid']))
    return ids


# unsafe, fails when disambiguation occurs
def download_and_save_from_wiki(name, ids):
    f = open(homePATH + name, 'w')
    length = len(ids)
    for num, id in enumerate(ids):
        print("now downloading " + str(num) + " out of " + str(length))
        page = wikipedia.page(pageid=id)
        f.write(page.content)
    f.close()


# safe, writes disambiguated articles to a file
def download_and_save_from_wiki(name, ids, startpoint):
    file = open(homePATH + name, 'w')
    disambiguation = open(homePATH + "DIS" + name, 'w')
    length = len(ids[startpoint:])
    for num, id in enumerate(ids[startpoint:]):
        print("Now downloading " + str(num) + " out of " + str(length))
        try:
            page = wikipedia.page(pageid=id)
            file.write(page.content)
        except wikipedia.DisambiguationError:
            DisambiguationErrorItems.append(id)
    for id in DisambiguationErrorItems:
        disambiguation.write(id)
        disambiguation.write("\n")
    file.close()
    disambiguation.close()
