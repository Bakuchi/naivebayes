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


def download_and_save_from_wiki(name, ids):
    f = open(homePATH + name, 'w')
    length = len(ids[273:])
    for num, id in enumerate(ids[273:]):
        print("now downloading " + str(num) + " out of " + str(length))
        page = wikipedia.page(pageid=id)
        f.write(page.content)
    f.close()


def continue_download(name, ids, startpoint):
    f = open(homePATH + name, 'w')
    dis = open(homePATH + "DIS" + name, 'w')
    length = len(ids[startpoint:])
    for num, id in enumerate(ids[startpoint:]):
        print("now downloading " + str(num) + " out of " + str(length))
        try:
            page = wikipedia.page(pageid=id)
            f.write(page.content)
        except wikipedia.DisambiguationError:
            DisambiguationErrorItems.append(id)
    for id in DisambiguationErrorItems:
        dis.write(id)
    f.close()
    dis.close()
# continue_download("relig", read_pageids(religionCSV),1621)
# continue_download("astro", read_pageids(astronomicCSV),1591)
# download_and_save_from_wiki("relig", read_pageids(religionCSV))
# download_and_save_from_wiki("astro", read_pageids(astronomicCSV))