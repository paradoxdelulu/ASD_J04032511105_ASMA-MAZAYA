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
def pangkat(a, n): 
    # Base case 
    if n == 0: 
        return 1 
    # Recursive case 
    return a * pangkat(a, n - 1) 
print(pangkat(2, 4))  # Output: 16 (2^4 = 2 * 2 * 2 * 2 = 16)