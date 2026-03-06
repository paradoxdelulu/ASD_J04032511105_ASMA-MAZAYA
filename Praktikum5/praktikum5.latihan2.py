#=============================================================
# Nama  : Asma Mazaya
# NIM   : J0403251105
# Kelas : A1
#=============================================================

# ========================================================== 
# Latihan 2: Tracing Rekursi 
# ==========================================================

def countdown(n): 
 
    if n == 0: 
        print("Selesai") 
        return 
 
    print("Masuk:", n) 
 
    countdown(n - 1) 
 
    print("Keluar:", n) 
 
 
countdown(3) 

# output 'Keluar' akan muncul terbalik dengan 
#'Masuk' karena proses unwinding terjadi setelah 
# semua pemanggilan rekursif selesai.