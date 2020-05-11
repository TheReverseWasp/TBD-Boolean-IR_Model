import json
import re

import spacy
sp = spacy.load('en_core_web_sm')

nlp = spacy.load('en', disable=['parser', 'ner'])

all_stopwords = sp.Defaults.stop_words
allowed = "abcdefghijklmnopqrstuvwxyzñ"

def get_filenames():
    filenames = []
    with open("../Datos/00_other/fnames.json", "r") as js:
        dict1 = json.load(js)
        filenames = dict1["filenames"]
    return filenames

def check_line(str_line):
    str_line = str_line.lower()
    temp = str_line
    str_line = re.split(r'[\t ]+', str_line)
    #print(len(str_line))
    for i in range(len(str_line) - 1):
        for j in str_line[i]:
            if allowed.find(j) == -1:
                return False
    return temp

def check_stop(str_line):
    text_tokens = re.split(r'[\t ]+', str_line)
    tokens_without_sw= [word for word in text_tokens if not word in all_stopwords]
    if len(tokens_without_sw) != 3:
        return False
    answer = " ".join(tokens_without_sw)
    return answer

def check_lemma(str_line):
    sentence = str_line
    doc = nlp(sentence)
    return " ".join([token.lemma_ for token in doc])

def get_words(str_line):
    text_tokens = re.split(r'[\t ]+', str_line)
    return text_tokens[:-1]

def join_dics_to_list(dic1, dic2):
    dic_general = {}
    for k, v in dic1:
        dic_general[k] = v
    for k, v in dic2:
        dic_general[k] = v
    answer = []
    for k, v in dic_general:
        answer.append(k)
    return answer

def distance(dic1, dic2, doc_list):
    count = 0
    for i in doc_list:
        if dic1[i] == True and dic2[i] == True:
            count += 1
    return count / len(doc_list)
