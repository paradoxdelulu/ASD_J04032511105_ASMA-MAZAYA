#=============================================================
# Nama  : Asma Mazaya
# NIM   : J0403251105
# Kelas : A1
#=============================================================

# ========================================================== 
# Latihan 1: Rekursi Pangkat 
# ========================================================== 
# Fungsi untuk menghitung a^n menggunakan rekursi
# Base case: a^0 = 1
# Recursive case: a^n = a * a^(n-1) untuk n > 0
def pangkat(a, n): # Fungsi rekursif untuk menghitung a pangkat n
    # Base case 
    if n == 0: 
        return 1 
    # Recursive case 
    return a * pangkat(a, n - 1) # Memanggil fungsi pangkat dengan n-1 untuk menghitung a pangkat n-1, lalu mengalikan hasilnya dengan a untuk mendapatkan a pangkat n
print(pangkat(2, 4))  # Output: 16 (2^4 = 2 * 2 * 2 * 2 = 16)