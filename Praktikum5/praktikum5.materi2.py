#=============================================================
# Nama  : Asma Mazaya
# NIM   : J0403251105
# Kelas : A1
#=============================================================

# ========================================================== 
# Contoh Rekursi 2: Tracing Masuk/Keluar 
# ========================================================== 
def hitung(n): 
# Base case 
# Ketika n mencapai 0, kita berhenti melakukan pemanggilan rekursif dan mulai proses unwinding.
    if n == 0: 
        print("Selesai") 
        return 
    print("Masuk:", n)      
    hitung(n - 1)            
    print("Keluar:", n)     
hitung(3) 
# fase stacking 
# pemanggilan rekursif 
# fase unwinding