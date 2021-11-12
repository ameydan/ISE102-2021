import copy

def dict_creation():
    print("********* Dictionary creation and access *********")
    a_dict = {}
    a_dict["Tolga"] = 4564564
    a_dict["Tolga"] = 564653
    print(a_dict["Tolga"])

    a_dict = {"Tolga Ovatman": "15/08/1979",
              "Duygu Ozkan": "12/12/1988",
              "Ozlem Aydın": "05/01/1999"}

    print(a_dict.get("Tolga", "01/01/1970"))
    print(a_dict)
    print("********* Dictionary creation and access *********")


def dict_iteration():
    print("********* Dictionary iteration *********")

    a_dict = {"Tolga Ovatman": "15/08/1979",
              "Duygu Ozkan": "12/12/1988",
              "Ozlem Aydın": "05/01/1999"}

    for tup in a_dict.items():
        print(tup)

    for key in a_dict.keys():
        print(key, "-->", a_dict[key])

    for value in a_dict.values():
        print(value)

    if "Tolga" in a_dict.keys() or "16/08/1979" in a_dict.values():
        print("Found!!!")
    else:
        print("Not Found!!!")

    a_dict["Murat Yılmaz"] = a_dict["Tolga Ovatman"]
    print(len(a_dict.keys()))

    b_dict = {"A": [1, 2, 3, 4]}
    #b_dict["B"] = b_dict["A"].copy()
    #b_dict["B"][0] = 100
    #print(b_dict)

    #c_dict = b_dict
    #c_dict = b_dict.copy()
    c_dict = copy.deepcopy(b_dict)
    c_dict["A"][0] = 100
    print(b_dict)
    print("********* Dictionary iteration *********\n")
