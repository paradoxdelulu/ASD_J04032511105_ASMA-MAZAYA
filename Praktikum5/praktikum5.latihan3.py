# ========================================================== 
# Latihan 3: Mencari Nilai Maksimum 
# ========================================================== 
 
def cari_maks(data, index=0): # Fungsi rekursif untuk mencari nilai maksimum dalam list
 
    # Base case 
    if index == len(data) - 1: # Jika sudah mencapai elemen terakhir, kembalikan elemen tersebut sebagai nilai maksimum
        return data[index] # Kembalikan elemen terakhir sebagai nilai maksimum karena tidak ada elemen lain yang tersisa untuk dibandingkan
 
    # Recursive case 
    maks_sisa = cari_maks(data, index + 1) # Cari nilai maksimum dari sisa list (elemen setelah index saat ini) dengan memanggil fungsi cari_maks secara rekursif dengan index yang ditingkatkan sebesar 1
    # Bandingkan nilai saat ini dengan nilai maksimum dari sisa list dan kembalikan yang lebih besar
    if data[index] > maks_sisa: # Jika nilai saat ini lebih besar dari nilai maksimum yang ditemukan di sisa list, kembalikan nilai saat ini sebagai nilai maksimum
        return data[index] # Kembalikan nilai saat ini sebagai nilai maksimum karena lebih besar dari nilai maksimum yang ditemukan di sisa list
    else: 
        return maks_sisa 
 
 
angka = [3, 7, 2, 9, 5] # Contoh list angka untuk mencari nilai maksimum
print("Nilai maksimum:", cari_maks(angka)) # Output: Nilai maksimum: 9 (9 adalah nilai terbesar dalam list angka)

