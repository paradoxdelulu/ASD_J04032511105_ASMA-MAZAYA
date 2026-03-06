#=============================================================
# Nama  : Asma Mazaya
# NIM   : J0403251105
# Kelas : A1
#=============================================================

#=============================================================
# Contoh Rekursi 1: Faktorial
#=============================================================

def faktorial(n): 
    # Base case: berhenti ketika n = 0
    # Faktorial dari 0 adalah 1 (0! = 1)
    # Jika n = 0, kembalikan 1 sebagai hasilnya
    if n == 0: 
        return 1 
    
    # Recursive case: masalah diperkecil menjadi faktorial(n-1) 
    return n * faktorial(n - 1)  # Memanggil fungsi faktorial dengan n-1 untuk menghitung faktorial dari n-1, lalu mengalikan hasilnya dengan n untuk mendapatkan faktorial dari n
print(faktorial(5))  # Output: 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)