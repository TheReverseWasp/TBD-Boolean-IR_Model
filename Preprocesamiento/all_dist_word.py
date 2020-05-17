from complementos import *

def main():
    dictionaryC = {}
    with open("../Datos/00_other/dictionaryC.json", "r") as jsfile:
        dictionaryC = json.load(jsfile)
    diclist = [key for key, value in dictionaryC.items()]
    #print(diclist)
    prevpath = "../Datos/04_words_data_s/"
    #print("key", i, diclist[i])
    while True:
        d1 = {}
        answer = {}
        print("ingrese la palabra")
        word = input()
        lemma_w = str(lemmatize_this(word))
        with open(prevpath + lemma_w + ".json", "r") as dic1:
            d1 = json.load(dic1)
        for j in range(len(diclist)):
            if j % 1000 == 0:
                print ("it: " + str(j) + " out of " + str(len(diclist)))
            if diclist[j] != lemma_w:
                d2 = {}
                with open(prevpath + diclist[j] + ".json", "r") as dic2:
                    d2 = json.load(dic2)
                d1d2l = join_dics_to_list(d1, d2)
                dist = calc_distance_bool(d1,d2,d1d2l)
                answer[diclist[j]] = dist
        with open("../Resultados/distancias/" + lemma_w + ".json", "w") as outquery1:
            json.dump(answer, outquery1)
            #return True

if __name__ == "__main__":
    main()
