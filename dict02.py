daftar_harga = [
    {"nama": "apel", "harga": 10000}, 
    {"nama": "jeruk", "harga": 20000},
    {"nama": "durian", "harga": 120000},
    {"nama": "kiwi", "harga": 60000},
    {"nama": "melon", "harga": 300000},
]

# tampilkan semua nama buah dan harganya
for buah in daftar_harga:
    print(f'{buah["nama"]} - {buah["harga"]}')

# tampilkan nama buah yang paling mahal
harga_termahal = 0
nama_buah_termahal = ''
for buah in daftar_harga:
    if buah['harga'] > harga_termahal:
        harga_termahal = buah['harga']
        nama_buah_termahal = buah["nama"]
print(f"Nama buah termahal adalah {nama_buah_termahal} dengan harga {harga_termahal}")

# hapus buah yang harganya < 100000
batas_harga = 100000

# ambil jumlah harga dalam list
count = len(daftar_harga)
index = 0
while index < count:
    if daftar_harga[index]["harga"] < batas_harga:
        del daftar_harga[index]
    else:
        index = index + 1
        count = len(daftar_harga)
'''
for index in range(len(daftar_harga)):
    if daftar_harga[index]['harga'] < batas_harga:
        del daftar_harga[index]
'''
        
# tampilkan semua nama buah dan harganya
print("Setelah semua buah di bawah batas harga dihapus")
for buah in daftar_harga:
    print(f'{buah["nama"]} - {buah["harga"]}')
