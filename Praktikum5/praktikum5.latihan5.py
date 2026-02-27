#=============================================================
# Nama  : Asma Mazaya
# NIM   : J0403251105
# Kelas : A1
#=============================================================

# ========================================================== 
# Studi Kasus: Generator PIN 
# ========================================================== 
 
def buat_pin(panjang, hasil=""): 
 
    if len(hasil) == panjang: 
        print("PIN:", hasil) 
        return # Base case: jika panjang PIN sudah tercapai, cetak hasil dan kembali
 
    for angka in ["0", "1", "2"]: 
        buat_pin(panjang, hasil + angka) 
 
 
buat_pin(3) 
# untuk mencegah angka yang sama muncul berulang kali, 
# kita bisa menggunakan set untuk menyimpan PIN yang sudah dibuat 
# dan memeriksa apakah PIN baru sudah ada dalam set sebelum mencetaknya. 