from complementos import *

def main():
    filenames = get_filenames()
    fnumber = 0
    documentos = {}
    for i in filenames:
        print("filenumber: " + str(fnumber))
        fnumber += 1
        with open("../Datos/01_Cleaned_data/without_stop/" +  i, "r") as fgc:
            lines = fgc.readlines()
            it = 1
            for j in lines:
                words = get_words(j)
                for k in words:
                    documentos[k] = True
                if it % 100000 == 0:
                    print("it: " + str(it))
                it += 1
    with open("../Datos/00_other/documentos.json", "w") as json_file:
        json.dump(documentos, json_file)

if __name__ == "__main__":
    main()
