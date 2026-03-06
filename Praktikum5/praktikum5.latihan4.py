#=============================================================
# Nama  : Asma Mazaya
# NIM   : J0403251105
# Kelas : A1
#=============================================================

# ========================================================== 
# Latihan 4: Kombinasi Huruf 
# ========================================================== 
 
def kombinasi(n, hasil=""): 
 
    if len(hasil) == n: 
        print(hasil) 
        return 
 
    kombinasi(n, hasil + "A") 
    kombinasi(n, hasil + "B") 
 
 
kombinasi(2) 
# Output: AA, AB, BA, BB (semua kombinasi huruf A dan B dengan panjang 2)
# Fungsi kombinasi akan menghasilkan semua kemungkinan kombinasi huruf 'A' dan 'B' dengan panjang n.
# Pada contoh di atas, kombinasi(2) akan menghasilkan semua kombinasi huruf 'A' dan 'B' dengan panjang 2, yaitu: AA, AB, BA, BB.
# Prosesnya bekerja dengan menambahkan 'A' atau 'B' ke string
# hasil secara rekursif hingga panjang string mencapai n, pada saat itu hasil akan dicetak.