data = {"genap": [], "ganjil;": []}
while True:
    angka = int(input("Masukkan angka [negatif untuk berhenti]: "))
    # jika negatif maka program selesai
    if angka < 0:
        break
    else:
        # Kelompokkan angka ganjil dan genap
        # 1. ganjil atau genap
        if angka % 2 == 0: # genap
            data["genap"].append(angka)
        else:
            data["ganjil"].append(angka)
print(data)