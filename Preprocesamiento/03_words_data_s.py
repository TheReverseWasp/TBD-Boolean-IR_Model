from complementos import *

def main():
    filenames = get_filenames()
    fnumber = 0
    documentos = {}
    with open("../Datos/00_other/documentos.json", "r") as json_file:
        documentos = json.data(json_file)
    for key, value in documentos:
        term = {}
        for i in filenames:
            with open("../Datos/01_Cleaned_data/without_stop/" +  i, "r") as fgc:
                lines = fgc.readlines()
                for j in lines:
                    data = check_term(key)
                    if data != False
                        term[data[0]] = data[1]
        with open("../Datos/03_words_data_s/" + key + ".json", "w") as json_term:
            json.dump(term, json_term)

if __name__ == "__main__":
    main()
