from complementos import *

def main():
    print(" 1. Busqueda individual, \n 2. Busqueda multipalabra")
    opcion = int(input())
    while opcion == 1 or opcion == 2:
        if opcion == 1:
            print("ingrese la palabra")
            word = input()
            lemma_w = str(lemmatize_this(word))
            try:
                d1 = {}
                #print(type(lemma_w))
                with open("../Datos/04_words_data_s/" + lemma_w + ".json", "r") as dic1:
                    d1 = json.load(dic1)

                to_sort = [[key, val[0]/val[1]] for key, val in d1.items()]
                #print(to_sort)
                #return 0
                #print(to_sort[0])
                to_sort.sort(key = lambda x: x[1])
                print(to_sort)
            except:
                print("la palabra no existe en el diccionario")
        else:
            print("ingrese el numero de las palabras a comparar")
            palabras_comp = int(input())
            dic_list = []
            word_list = []
            i = 0
            while i < palabras_comp:
                print("palabra", i, "de", palabras_comp)
                try:
                    print("ingrese la palabra")
                    word = input()
                    lemma_w = str(lemmatize_this(word))
                    d1 = {}
                    with open("../Datos/04_words_data_s/" + lemma_w + ".json", "r") as dic1:
                        d1 = json.load(dic1)
                    dic_list.append(d1)
                    word_list.append(lemma_w)
                    i += 1
                except:
                    print("palabra errada inserte otra")
            #print(len(dic_list))
            result = magic_fun(word_list, dic_list)
            with open("../Resultados/results_sc.txt", "w") as res1:
                for i in result:
                    res1.write(str(i) + "\n")
        print(" 1. Busqueda individual, \n 2. Busqueda multipalabra")
        opcion = int(input())

if __name__ == "__main__":
    main()
