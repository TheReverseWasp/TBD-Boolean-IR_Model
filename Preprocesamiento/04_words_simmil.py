from complementos import *

def main():
    filenames = get_filenames()
    fnumber = 0
    documentos = {}
    with open("../Datos/00_other/documentos.json", "r") as json_file:
        documentos = json.data(json_file)
    for key1, value1 in documentos:
        term = {}
        with open("../Datos/03_words_data_s/" + key1 + ".json") as term1:
            term = json.load(term1)
        for key2, value2 in documentos:
            if key1 != key2:
                term_to_compare = {}
                with open("../Datos/03_words_data_s/" + key2 + ".json") as term1:
                    term_to_compare = json.load(term1)
                list_of_common = join_dics_to_list(term, term_to_compare)
                


if __name__ == "__main__":
    main()
