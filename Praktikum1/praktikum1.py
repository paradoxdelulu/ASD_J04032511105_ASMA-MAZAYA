#=============================================================
# Nama  : Asma Mazaya
# NIM   : J0403251105
# Kelas : A1
#=============================================================

#Praktikum 1 : Konsep ADT dan File Handling
#Latihan dasar 1 : Membaca seluruh isi file data

print("Membuka file dalam satu string")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)
print(f"tipe data: {type(isi_file)}")

#Ngebuka file per baris dalam list

print("Membuka file dalam list per baris")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        print(f"Baris ke: {jumlah_baris}")
        print(f"isinya: {baris}")

#Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom-kolom data

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print(f"NIM: {nim} | Nama: {nama} | Nilai: {nilai}")
    

data_list = []

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_list.append([nim, nama, int(nilai)])
print("Data Mahasiswa:")
print(data_list)
print("Contoh record ke 1", data_list[0])
print("Contoh record ke 2", data_list[1])
print("Jumlah Record:", len(data_list))

#Praktikum 1 : Konsep ADT dan File Handling
#Latihan dasar 4 : Mmebaca Data dan Menyimpannya dalam Bentuk Dictionarypannya 
data_dict = {}

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_dict[nim] = {
            "nama": nama, 
            "nilai": int(nilai)
            }
print("Data Mahasiswa dalam Dictionary:")
print(data_dict)
