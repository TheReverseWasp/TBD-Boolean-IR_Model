
import json

def main():
    print("ingrese la palabra")
    d1 = {}
    word = input()
    with open("../Resultados/distancias/" + word + ".json", "r") as js1:
        d1 = json.load(js1)
    l1 = [[key, val] for key, val in d1.items()]
    l1.sort(key = lambda x: x[1])
    index = len(l1) - 1
    for i in range(len(l1)):
        print(index, l1[i])
        index -= 1

if __name__ == "__main__":
    main()
