from complementos import *

def main():
    filenames = get_filenames()
    fnumber = 0
    for i in filenames:
        print("filenumber: " + str(fnumber))
        fnumber += 1
        with open("../Datos/00_GC_data/" +  i, "r") as fgc:
            with open("../Datos/01_Cleaned_data/without_symbols/" +  i, "w") as clgc:
                lines = fgc.readlines()
                it = 1
                for j in lines:
                    answer = check_line(j)
                    if answer != False:
                        clgc.write(answer)
                    if it % 100000 == 0:
                        print("it: " + str(it))
                    it +=1

if __name__ == "__main__":
    main()
