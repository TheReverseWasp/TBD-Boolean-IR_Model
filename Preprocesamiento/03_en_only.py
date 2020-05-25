from complementos import *

#Script de limpieza final que verifica si las palabras dentro de los archivos estan en ingles
#(ejecucion obligatoria)
#guarda los archivos dentro de ../Datos/03_en_only/ con el mismo nombre del corpus

def main():
    filenames = get_filenames()
    print("file inicio")
    ini = int(input())
    print("file final")
    fin = int(input())
    fnumber = ini
    for i in range(ini, fin + 1):
        print("filenumber: " + str(fnumber))
        fnumber += 1
        with open("../Datos/02_lemma_data/" +  filenames[i], "r") as fgc:
            with open("../Datos/03_en_only/" +  filenames[i], "w") as clgc:
                lines = fgc.readlines()
                it = 1
                for j in lines:
                    answer = check_en(j)
                    if answer != False:
                        clgc.write(answer)
                    if it % 1000 == 0:
                        print("it: " + str(it) + " out of " + str(len(lines)))
                    it += 1

if __name__ == "__main__":
    main()
