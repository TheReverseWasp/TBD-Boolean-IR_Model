from complementos import *

#Script de generacion de palabras correlacionadas a cada palabra
#genera un json por cada palabra
#ejecucion obligatoria

def main():
    filenames = get_filenames()
    fnumber = 0
    words = {}
    word_json_list = {}
    for i in range(len(filenames)):
        print("filenumber: " + str(fnumber))
        fnumber += 1
        with open("../Datos/03_en_only/" +  filenames[i], "r") as fen:
            lines = fen.readlines()
            it = 0
            for l in lines:
                if it % 10000 == 0:
                    print("it: " + str(it) + " out of " +str(len(lines)))
                it += 1
                sptk = separar_elems(l)
                #print(sptk)
                words[sptk[0]] = True
                if sptk[0] in word_json_list:
                    if sptk[-3] in word_json_list[sptk[0]]:
                        word_json_list[sptk[0]][sptk[-3]][0] += int(sptk[-2])
                        word_json_list[sptk[0]][sptk[-3]][1] += 1
                    else:
                        word_json_list[sptk[0]][sptk[-3]] = [int(sptk[-2]), 1]
                else:
                    word_json_list[sptk[0]] = {sptk[-3]: [int(sptk[-2]), 1]}
            #print(str(word_json_list))
            for key, val in word_json_list.items():
                print("key: ", key)
                #print(str(word_json_list[key]))
                with open("../Datos/04_words_data_s/" + key + ".json", "w") as jsonf2:
                    json.dump(word_json_list[key], jsonf2)
            word_json_list = {}

    with open("../Datos/00_other/dictionaryC.json", "w") as jsonf1:
        json.dump(words, jsonf1)

if __name__ == "__main__":
    main()
