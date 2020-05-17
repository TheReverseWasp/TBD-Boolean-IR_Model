from complementos import *

def main():
    dictionaryC = {}
    with open("../Datos/00_other/dictionaryC.json", "r") as jsfile:
        dictionaryC = json.load(jsfile)
    diclist = [key for key, value in dictionaryC.items()]
    #print(diclist)
    prevpath = "../Datos/04_words_data_s/"
    print("limmit: " + str(len(diclist)))
    print("inicio")
    ini = int(input())
    print("fin")
    fin = int(input())
    for i in range(ini, fin + 1):
        print("key", i, diclist[i])
        d1 = {}
        answer = {}
        with open(prevpath + diclist[i] + ".json", "r") as dic1:
            d1 = json.load(dic1)
        for j in range(len(diclist)):
            if j % 80000 == 0:
                print ("it: " + str(j) + " out of " + str(len(diclist)))
            if i != j:
                d2 = {}
                with open(prevpath + diclist[j] + ".json", "r") as dic2:
                    d2 = json.load(dic2)
                d1d2l = join_dics_to_list(d1, d2)
                dist = calc_distance_bool(d1,d2,d1d2l)
                answer[diclist[j]] = dist
        with open("../Datos/05_words_simmil/" + diclist[i] + ".json", "w") as outquery1:
            json.dump(answer, outquery1)
        #return True

if __name__ == "__main__":
    main()
