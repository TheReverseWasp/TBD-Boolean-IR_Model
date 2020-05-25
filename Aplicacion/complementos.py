import json
import re
import spacy
import enchant
import copy as cp

d = enchant.Dict("en_US")

sp = spacy.load('en_core_web_sm')

#nlp = spacy.load('en', disable=['parser', 'ner'])

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
    doc = sp(sentence)
    return " ".join([token.lemma_ for token in doc])

def get_words(str_line):
    text_tokens = re.split(r'[\t ]+', str_line)
    return text_tokens[:-1]

def lemmatize_this(str_word):
    return sp(str_word)[0]

def check_en(str_line):
    text_tokens = re.split(r'[\t ]+', str_line)
    if d.check(text_tokens[0]) == False or d.check(text_tokens[1]) == False:
        return False
    return str_line

def separar_elems(str_line):
    text_tokens = re.split(r'[\t \n]+', str_line)
    #print(len(text_tokens))
    return text_tokens

def join_dics_to_list(dic1, dic2):
    dic_general = {}
    for k, v in dic1.items():
        dic_general[k] = v
    for k, v in dic2.items():
        dic_general[k] = v
    answer = []
    for k, v in dic_general.items():
        answer.append(k)
    return answer

def calc_distance_bool(dic1, dic2, doc_list):
    count = 0
    for i in doc_list:
        if dic1.get(i, False) != False and dic2.get(i, False) != False:
            count += 1
    #print(count, len(doc_list))
    return count / len(doc_list)

def calc_distance_normal(dic1, dic2, doc_list):
    acum = 0
    for i in doc_list:
        if dic1.get(i, False) == False:
            acum += (dic2[i][0]/dic2[i][1]) ** 2
        elif dic2.get(i, False) == False:
            acum += (dic1[i][0]/dic1[i][1]) ** 2
        else:
            acum += (dic1[i][0]/dic1[i][1] - dic2[i][0]/dic2[i][1]) ** 2
    #print(count, len(doc_list))
    return acum ** .5

def join_list_to_dict(l1, d1):
    dt = {}
    for i in l1:
        dt[i] = True
    return join_dics_to_list(dt, d1)

def magic_fun(word_list, dic_list):
    final_list = join_dics_to_list(dic_list[0], dic_list[1])
    for i in range(2, len(word_list)):
        final_list = join_list_to_dict(final_list, dic_list[i])
    answer = []
    temp = ["               "]
    for i in word_list:
        temp.append(i)
    answer.append(temp)
    for i in final_list:
        temp = [i]
        for j in dic_list:
            if j.get(i, False) == False:
                temp.append(0)
            else:
                temp.append(1)
        answer.append(temp)
    return answer
