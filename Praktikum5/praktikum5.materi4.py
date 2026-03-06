#=============================================================
# Nama  : Asma Mazaya
# NIM   : J0403251105
# Kelas : A1
#=============================================================

# ========================================================== 
# Contoh Backtracking 1: Kombinasi Biner (n) 
# ========================================================== 
def biner(n, hasil=""): 
# Base case: jika panjang string sudah n, cetak hasil 
    if len(hasil) == n: 
        print(hasil) 
    # Recursive case: tambahkan '0' atau '1' ke hasil dan lanjutkan pencarian
        return
    # Choose + Explore: tambah '0' 
    biner(n, hasil + "0") 
    
        # Choose + Explore: tambah '1' 
    biner(n, hasil + "1") 
    
biner(3)