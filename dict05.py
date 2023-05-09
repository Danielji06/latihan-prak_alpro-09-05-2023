data = dict()
while True:
    angka = int(input("Masukkan angka [negatif untuk berhenti]: "))
    # jika negatif maka program selesai
    if angka < 0:
        break
    else:
        # Kelompokkan angka ganjil dan genap
        # 1. ganjil atau genap
        if angka % 2 == 0: # genap
            if data.get("genap") != None:
                data["genap"].append(angka)
            else:
                data["genap"] = [angka]
        else:
            if data.get("ganjil") != None:
                data["ganjil"].append(angka)
            else:
                data["ganjil"] = [angka]
print(data)