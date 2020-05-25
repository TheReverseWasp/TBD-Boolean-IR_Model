import json

def main():
    root_part = "2gm-"
    json_dict = {"filenames": []}
    for i in range(32):
        temp = str(i)
        while(len(temp) < 4):
            temp = "0" + temp
        json_dict["filenames"].append(root_part + temp)
    with open("../Datos/00_other/fnames.json", "w") as json_file:
        json.dump(json_dict, json_file)

if __name__ == "__main__":
    main()
