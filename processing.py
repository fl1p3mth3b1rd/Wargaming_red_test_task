from bson.json_util import dumps
from math import log10
from pymongo import MongoClient, DESCENDING

client = MongoClient("mongodb://localhost:27017/")
db = client.war_gaming_red_task

def count_TF_IDF(file):
    hash_table = {}
    try:
        text = file.read().decode('utf-8').split()
    except MemoryError:
        return "Файл слишком большой. Попробуйте разбить его на части и попробуйте снова."
    if not text:
        return 'Пустой файл недопустим'
    unique_words = set(text)
    for word in unique_words:
        hash_table[word] = {'TF' : text.count(word)}
    db.docs.insert_one(count_IDF(unique_words, hash_table))
    all_words = db.docs.find({}, {'_id':0}).sort('_id', -1).limit(1)
    sorted_by_idf = {k : v for k,v in sorted(all_words[0].items(), key=lambda item: item[1]['IDF'], reverse=True)}
    return list(sorted_by_idf.items())[:50]

def count_IDF(unique_words, hash_table):
    number_of_docs = db.docs.count()
    number_of_docs += 1
    count = 1
    for word in unique_words:
        for doc in db.docs.find({}):
            if doc.get(word):
                count +=1
        idf = round(log10(number_of_docs/count), 3)
        hash_table[word]['IDF'] = idf
        count = 1
    return hash_table
